"""
This checks if the version of each image needs to be updated, and if so, updates the version of the image.
"""

import os
import logging
import hashlib
import traceback
from typing import Literal

import toml
from awesomeversion import AwesomeVersion

from . import util
from .config import config
from .ruyi_index_parser import PackageIndexProc, clone_package_index
from .ruyi_index_parser import BoardImages
from ..matrix_parser import Systems, ImageStatus
from ..matrix_parser import VInfo, gen_oldver
from .plugin_handler import find_plugin
from .upload_plugin_base import UploadPluginBase

logger = logging.getLogger(__name__)


def cmp_version(v1: str, v2: str) -> int:
    """
    Compare the version of two strings
    """
    av1 = AwesomeVersion(v1)
    av2 = AwesomeVersion(v2)
    if av1 > av2:
        return 1
    if av1 < av2:
        return -1
    return 0


class BoardImageWrapper:
    """
    Hold the operations on the board image index
    """

    def __init__(self,
                 vinfo: VInfo,
                 plugin: UploadPluginBase,
                 index_name: str,
                 old_indexs: list[BoardImages]
                 ):
        self.vinfo = vinfo
        self.plugin = plugin
        self.index_name = index_name
        self.old_indexs = old_indexs

        if len(self.old_indexs) <= 0:
            self.old_indexs.append(self.__gen_dummy_index(
                vinfo.vendor
            ))

        self.index = self.plugin.handle_report(
            self.vinfo, self.index_name, self.old_indexs)

    def __gen_dummy_index(self, name: str = "Dummy", strategy: str = "dd-v1") -> BoardImages:
        """
        Generate a dummy index
        """
        return BoardImages(
            bot_created=False,
            version="0.0.0",
            info={
                    "format": "v1",
                    "metadata": {
                        "desc": "Dummy file",
                        "vendor": {
                            "name": name,
                            "eula": ""
                        },
                    },
                "distfiles": [],
                "blob": {
                        "distfiles": []
                    },
                "provisionable": {
                        "strategy": strategy,
                        "partition_map": None
                    }
            }
        )

    def new_index(self) -> BoardImages:
        """
        Generate the new index
        """
        return self.index

    def new_index_name(self) -> str:
        """
        Generate the new index file name
        """
        return f"{self.index.version}.toml"

    def new_index_dict(self) -> dict:
        """
        Generate the new index dict
        """
        return self.index.serialize()

    def new_index_toml(self) -> str:
        """
        Generate the new index toml
        """
        return toml.dumps(self.new_index_dict())

    def gen_hash(self) -> str:
        """
        Generate the hash of the new index, used to identify the pr
        """
        h = hashlib.sha224(
            self.new_index_toml().encode("utf-8") + self.new_index_name().encode("utf-8")
        )
        return h.hexdigest()


class RuyiDiff:
    """
    A wrapper for RuyiDiff, holding the resource, doing the diff process
    """

    class RuyiUpdateInfo:
        """
        Information of the update on a single image
        """
        stat: Literal['none', 'update', 'nochange', 'error']
        force: bool | None
        old_ver: str | None
        new_ver: str | None

        def __init__(self, stat: Literal['none', 'update', 'nochange', 'error'] = 'none',
                     force: bool | None = None,
                     old_ver: str | None = None, new_ver: str | None = None):
            self.stat = stat
            self.force = force
            self.old_ver = old_ver
            self.new_ver = new_ver

        def __str__(self):
            if self.stat == "none":
                return "No update handler found"
            if self.stat == "nochange":
                return f"No change for version {self.old_ver}"
            if self.stat == "update":
                return f"Update from {self.old_ver} to {self.new_ver}"
            if self.stat == "error":
                return "Error occurs when updating! Please check the log for more information"
            return "Unknown status"

    def __is_bootstrap(self, vinfo: VInfo, plug: UploadPluginBase):
        """
        Cross check if an index isn't exists of a vinfo. If true, means we are doing a bootstrap
        """
        index_name: str | None = None
        for k, v in plug.all_index_can_handle().items():
            if v == vinfo:
                index_name = k
                break

        if index_name is None:
            return False

        if index_name not in self.index:
            return True

    def __do_bootstrap(self, vinfo: VInfo, plug: UploadPluginBase):
        """
        Bootstrap a new index
        """
        new_index_names = []
        for k, v in plug.all_index_can_handle().items():
            if v == vinfo and k not in self.index:
                new_index_names.append(k)
        for name in new_index_names:
            logger.warning(
                "Bootstrapping a new image in packages index: %s", name)
            self.index = self.index_proc.create_new_index(self.index, name)

    def __yield_one_sys(self, vinfo: VInfo,
                        plug: UploadPluginBase):
        if self.__is_bootstrap(vinfo, plug):
            self.__do_bootstrap(vinfo, plug)
        for index_name, index in self.index.items():
            if not plug.is_mapped_ruyi_index(vinfo, index_name):
                continue

            newest_version = "0.0.0"
            for i in index:
                if cmp_version(i.version, newest_version) > 0:
                    newest_version = i.version

            matrix_version = plug.handle_version(vinfo)

            # Mark update info
            vinfo.update_info.stat = "nochange"
            vinfo.update_info.old_ver = newest_version

            if newest_version < matrix_version:
                logger.info(
                    "Find new version for %s: %s -> %s",
                    index_name, newest_version, matrix_version)

                # Update update info
                vinfo.update_info.stat = "update"
                vinfo.update_info.new_ver = matrix_version

                yield BoardImageWrapper(vinfo, plug, index_name, index)
            elif config["force"]:
                logger.info(
                    "Force update for %s: %s -> %s",
                    index_name, newest_version, matrix_version)

                # Update update info
                vinfo.update_info.stat = "update"
                vinfo.update_info.new_ver = matrix_version
                vinfo.update_info.force = True

                yield BoardImageWrapper(vinfo, plug, index_name, index)

    def gen_branch(self):
        """
        Yield the system that needs to be updated
        """
        threadhold = ImageStatus(config["threadhold"])
        filter_plugins = config["plugin_names"]
        for _, v in self.oldver.items():
            # Mark system update info

            setattr(v, "update_info", self.RuyiUpdateInfo())

            # Find the plugin that can handle the system
            plugin = find_plugin(v)
            if plugin is None:
                continue
            if filter_plugins is not None and len(filter_plugins) > 0 and \
                    plugin.get_name() not in filter_plugins:
                continue

            if v.raw_data.status < threadhold:
                logger.info("Image %s is blocked dueto status %s less then threadhold %s", repr(
                    v), v.raw_data.status, threadhold)
                continue

            logger.info("Processing %s...", repr(v))

            # Please notice:
            # One system may have multiple ruyi_index, we need to handle them all
            # So, we need to iterate the index

            try:
                yield from self.__yield_one_sys(v, plugin)
            except Exception as e:  # pylint: disable=broad-except
                v.update_info.stat = "error"
                logger.error("Error occurs when handling system %s:%s:%s-%s",
                             v.vendor, v.system, v.variant, v.version)
                logger.error("Error: %s", e)
                logger.error(traceback.format_exc())

    def update_info(self) -> list[tuple[str, str, str]]:
        """
        Generate the update info
        """
        res = []
        for _, v in self.oldver.items():
            i = ('/'.join(v.raw_data.link),
                 f"{v.vendor}-{v.system}-{v.variant}", str(v.update_info))
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
