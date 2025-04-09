"""
This checks if the version of each image needs to be updated, and if so, updates the version of the image.
"""

import os
import logging
import hashlib
import traceback
from typing import Generator, Literal

import toml
from ruamel.yaml import YAML

from ..ruyi_index_updator.index_handler import RuyiGitRepo
from . import util
from .config import config
from .schema.provisioner import ProvisionerConfig, ImageComboDecl
from .ruyi_index_parser import PackageIndexProc, clone_package_index
from .ruyi_index_parser import BoardImagesGenerator
from ..matrix_parser import Systems
from ..matrix_parser import SystemInfo, gen_oldver
from .plugin_handler import find_plugin
from .upload_plugin_base import UploadPluginBase

logger = logging.getLogger(__name__)


class SystemWorker:
    """
    Hold the git branch and corresponding actions of a system
    """

    # Some times vendor.name is provided by others, so it doesn't match board vendor. Inhert old vendor
    vendor_name: str | None = None

    def __init__(self, info: SystemInfo, plugin: UploadPluginBase, repo: RuyiGitRepo):
        self.info = info
        self.plugin = plugin
        self.repo = repo
        self.branch_name = f"{util.system_id(info, None)}-{"_".join(info.board_variants)}_update_branch"
        self.ident = ""

        self.repo.local_checkout(self.branch_name)

    def __enter__(self):
        self.repo.local_checkout(self.branch_name)
        return self

    def do_checkout(self):
        """
        Initialize the branch, not needed to be called in the context manager
        """
        self.repo.local_checkout(self.branch_name)

    def do_push(self):
        """
        Push the branch to the remote
        """
        self.repo.local_push(self.branch_name)

    def do_pr(self):
        """
        Create a PR
        """
        title = f"Bump image {self.info.system} in device {self.info.vendor} to version {self.info.version}"
        body = f"""
Bump image {self.info.system} in device {self.info.vendor} to version {self.info.version}

Ident: {self.ident}

This PR is created by program Sync Package Index inside support-matrix

{f"Run ID: {config['CI_RUN_ID']}\nRun URL: {config['CI_RUN_URL']}" if config["CI_RUN_ID"] is not None else ""}
"""
        self.repo.create_pr(title, body, self.branch_name, "main")

    def do_commit(self):
        """
        Commit the changes
        """
        self.repo.local_commit(
            f"Bump image {self.info.system} in device {self.info.vendor} to version {self.info.version}")

    def do_update(self):
        """
        Do the update
        """
        _ = """
        To update a system, there are several steps:
        - Update all its files to the newest version
        - For each boardd variant:

        """
        self.__update_manifests()
        self.__update_provisioner()

    def __update_provisioner(self):
        provisioner_path = os.path.join(
            self.repo.local_repo.working_dir,
            "provisioner",
            "config.yml"
        )
        yaml = YAML()
        yaml.indent(mapping=2, sequence=4, offset=2)
        yaml.preserve_quotes = True
        with open(provisioner_path, encoding="utf-8") as stream:
            provisioner: ProvisionerConfig = yaml.load(stream)

        image_combos: list[ImageComboDecl] = []
        variants_combos: dict[str, str] = {}

        vendor = self.info.vendor

        board_variants = self.info.board_variants or ["generic"]

        for board_variant in board_variants:
            variant_id = board_variant
            if board_variant == "generic":
                board_variant = None
            system_id = util.system_id(self.info, board_variant)
            system_display_name = self.plugin.system_display_name(
                self.info, board_variant)
            image_files = self.plugin.system_image_files(
                self.info, board_variant)
            system_packages = [
                f"board-image/{file}" for file in image_files
            ]
            image_combo: ImageComboDecl = {
                "id": system_id,
                "display_name": system_display_name,
                "packages": system_packages
            }
            image_combos.append(image_combo)

            variants_combos[variant_id] = system_id

        # union the image_combos
        new_combo_exist = [False for _ in range(len(image_combos))]
        for combo in provisioner["image_combos"]:
            for idx, new_combo in enumerate(image_combos):
                if combo["id"] == new_combo["id"]:
                    new_combo_exist[idx] = True
                    break
        for idx, exist in enumerate(new_combo_exist):
            if exist:
                continue
            provisioner["image_combos"].append(image_combos[idx])

        # if device not in devices, add it
        device_idx = None
        for idx, device in enumerate(provisioner["devices"]):
            if device["id"] == vendor:
                device_idx = idx
                break
        if device_idx is None:
            provisioner["devices"].append({
                "id": vendor,
                "display_name": self.info.product,
                "variants": []
            })
            device_idx = len(provisioner["devices"]) - 1

        # add the variant combos to the device if not exists
        for variant in board_variants:
            # first add the variant if not exists
            variant_idx = None
            for idx, v in enumerate(provisioner["devices"][device_idx]["variants"]):
                if v["id"] == variant:
                    variant_idx = idx
                    break
            if variant_idx is None:
                provisioner["devices"][device_idx]["variants"].append({
                    "id": variant,
                    "display_name": f"{self.info.product} ({variant})",
                    "supported_combos": []
                })
                variant_idx = len(
                    provisioner["devices"][device_idx]["variants"]) - 1
            # then add the image combos to the variant
            logger.info("Add combos to device %s, variant %s",
                        provisioner["devices"][device_idx]["id"],
                        provisioner["devices"][device_idx]["variants"][variant_idx]["id"]
                        )
            if variants_combos[variant] not in \
                    provisioner["devices"][device_idx]["variants"][variant_idx]["supported_combos"]:
                provisioner["devices"][device_idx]["variants"][variant_idx]["supported_combos"].append(
                    variants_combos[variant])

        # write back to the provisioner
        with open(provisioner_path, "w", encoding="utf-8") as f:
            yaml.dump(provisioner, f)

        self.repo.local_add(provisioner_path)

    def __update_manifests(self):
        new_manifests = self.plugin.handle_report(self.info)
        for file, new_manifest in new_manifests.items():
            print(f"Updating {file} to {new_manifest.version}")
            if isinstance(new_manifest, BoardImagesGenerator):
                new_manifest = new_manifest.generate(
                    self.plugin.handle_version(self.info)
                )
            if self.vendor_name is not None:
                new_manifest.info["metadata"]["vendor"]["name"] = self.vendor_name
            file_name = f"{new_manifest.version}.toml"
            file_path = os.path.join(
                self.repo.local_repo.working_dir,
                "manifests",
                "board-image",
                file,
                file_name
            )
            index_dir = os.path.dirname(file_path)
            os.makedirs(index_dir, exist_ok=True)

            # check does it need to update
            newest_version = "0.0.0-0"
            for f_name in os.listdir(index_dir):
                if not f_name.endswith(".toml"):
                    continue
                version = f_name[:-5]
                if util.cmp_version(version, newest_version) > 0:
                    newest_version = version
            if util.cmp_version(newest_version, new_manifest.version) >= 0:
                continue

            with open(file_path, "w", encoding="utf-8") as f:
                toml.dump(new_manifest.info, f)
                self.__update_ident(toml.dumps(new_manifest.info))
                if new_manifest.bot_created:
                    f.write(
                        "\n# This file is created by program Sync Package Index inside support-matrix\n"
                    )
                if config["CI_RUN_ID"] is not None:
                    f.write(f"# Run ID: {config['CI_RUN_ID']}\n")
                    f.write(f"# Run URL: {config['CI_RUN_URL']}\n")
            self.repo.local_add(file_path)

    def __update_ident(self, append: str):
        self.ident = hashlib.sha256(
            f"{self.ident} {append}".encode("utf-8")).hexdigest()


class RuyiDiff:
    """
    A wrapper for RuyiDiff, holding the resource, doing the diff process
    """

    class RuyiUpdateInfo:
        """
        Information of the update on a single image
        """
        stat: Literal['none', 'force', 'update', 'nochange', 'error']
        plug: str
        file_stat: dict[str, tuple[Literal['none',
                                           'update', 'nochange', 'error'], str]]

        def __init__(self, stat: Literal['none', 'update', 'nochange', 'error'] = 'none',
                     plug: str = "None",
                     force: bool | None = None):
            self.stat = stat
            self.plug = plug
            self.force = force
            self.file_stat = {}

        def __str__(self):
            if self.stat == "none":
                res = "No plugin can handle this system"
            elif self.stat == "force":
                res = "Force update"
            elif self.stat == "nochange":
                res = "Nothing changed"
            elif self.stat == "error":
                res = "Error occurs"
            else:
                res = "Updated"
            if len(self.file_stat) <= 0:
                return res

            # For updated system, try to generate a human-readable message
            res = ""
            for file, stat in self.file_stat.items():
                if stat[0] == "none":
                    app = f"{file}: Not supported"
                elif stat[0] == "force":
                    app = f"{file}: Force update"
                elif stat[0] == "nochange":
                    app = f"{file}: No change"
                elif stat[0] == "error":
                    app = f"{file}: Error occurs"
                else:
                    app = f"{file}: {stat[1]}"
                res += app + "<br/>"
            return res

    def __do_one_sys(self, info: SystemInfo,
                     plug: UploadPluginBase, repo: RuyiGitRepo):

        # So for an system, (maybe) multiple files are available.

        current_version = plug.handle_version(info)
        vendor_name = None
        if current_version is None:
            return

        files = plug.system_image_files(info)
        logger.info("Files: %s", files)
        if len(files) <= 0:
            return

        info.update_info.stat = "nochange"
        needs_update = False
        for file in files:
            file_exists = False
            for image_name, image_manifests in self.index.items():
                if image_name != file:
                    continue
                newest_version = "0.0.0-0"
                for image_manifest in image_manifests:
                    if util.cmp_version(image_manifest.version, newest_version) > 0:
                        newest_version = image_manifest.version
                    vendor_name = image_manifest.info["metadata"]["vendor"]["name"]

                if util.cmp_version(current_version, newest_version) > 0:
                    needs_update = True
                    info.update_info.stat = "update"
                    info.update_info.file_stat[file] = (
                        "update", f"{newest_version} -> {current_version}")
                else:
                    info.update_info.file_stat[file] = (
                        "nochange", f"{newest_version} -> {current_version}")
                file_exists = True
                break
            if not file_exists:
                needs_update = True
                info.update_info.stat = "update"
                info.update_info.file_stat[file] = (
                    "update", f"0.0.0-0 -> {current_version}")
        if config["force"]:
            needs_update = True
            info.update_info.stat = "force"

        if not needs_update:
            return
        res = SystemWorker(info, plug, repo)
        res.vendor_name = vendor_name
        yield res

    def gen_branch(self, repo: RuyiGitRepo) -> Generator[SystemWorker, None, None]:
        """
        Checkout to a new branch and do the stuff
        """
        filter_plugins = config["plugin_names"]
        for info in self.oldver:

            # Should we skip this system?
            if info.raw_data.last_update == "eol":
                continue
            if info.raw_data.raw_data.get("skip_sync", False):
                logger.info("Skip update for %s", repr(info))
                continue

            # Mark system update info

            setattr(info, "update_info", self.RuyiUpdateInfo())

            # Find the plugin that can handle the system
            plugin = find_plugin(info)
            if plugin is None:
                continue
            if filter_plugins is not None and len(filter_plugins) > 0 and \
                    plugin.get_name() not in filter_plugins:
                continue

            logger.info("Processing %s", repr(info))

            info.update_info.plug = plugin.get_name()
            try:
                yield from self.__do_one_sys(info, plugin, repo)
            except Exception as _:  # pylint: disable=broad-except
                info.update_info.stat = "error"
                logger.error(
                    "Error occurs when handling system %s", repr(info))
                logger.error(traceback.format_exc())

    def update_info(self) -> list[tuple[str, str, str]]:
        """
        Generate the update info
        """
        res = []
        for v in self.oldver:
            if not hasattr(v, "update_info"):
                continue
            i = ('/'.join(v.raw_data.link),
                 v.update_info.plug,
                 str(v.update_info))
            res.append(i)
        return res

    def __init__(self, matrix: Systems):
        self.tmp_path = util.folder_tmp_mux(config["CACHE_DIR"])
        index_path = os.path.join(self.tmp_path, "packages-index")
        self.repo = clone_package_index(index_path)
        self.index_proc = PackageIndexProc(index_path)
        self.index = self.index_proc.parse_board()
        self.matrix = matrix
        self.oldver = gen_oldver(matrix)

    def __enter__(self):
        return self
