# pylint: disable=import-outside-toplevel, unused-import
"""
Base class for upload plugins. 

**NOTICE** You shall use dynamic import in the plugin handler.

See lm4a_revy.py for example.
"""

from abc import ABC, abstractmethod

from ..matrix_parser import SystemIdentifier, SystemInfo
from .ruyi_index_parser import BoardImages, BoardImagesGenerator, DistfileDeclType


class UploadPluginBase(ABC):
    """
    A base interface for plugins
    """
    __version__: str = None
    __tmppath__: str = None

    import logging
    from src.ruyi_index_updator.ruyi_index_parser import BoardImagesGenerator
    from src.matrix_parser import SystemIdentifier, SystemInfo
    logger: logging.Logger

    # Following are the metadata of the plugin

    def __init__(self) -> None:
        self.logger = self.logging.getLogger(self.get_name())

    @staticmethod
    @abstractmethod
    def get_name() -> str:
        """
        Get the name of the plugin
        """
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"<Ruyi Index Updator Plugin: {self.get_name()}: v{self.__version__}>"

    def all_can_handle(self) -> list[SystemIdentifier]:
        """
        Give a list of all the index name from packages index which this plugin can process.
        """
        raise NotImplementedError

    # Following are how the plugin should handle a system

    @abstractmethod
    def system_display_name(self, info: SystemInfo, board_variant: str | None = None) -> str:
        """
        Get the display name of the system
        """
        raise NotImplementedError

    @abstractmethod
    def system_image_files(self, info: SystemInfo, board_variant: str | None = None) -> list[str]:
        """
        Get the image files of the system
        """
        raise NotImplementedError

    @abstractmethod
    def handle_version(self, info: SystemInfo) -> str | None:
        """
        Handle the version mapping from system version to Ruyi Index version.
        """
        raise NotImplementedError

    @abstractmethod
    def handle_report(self,
                      info: SystemInfo) -> dict[str, BoardImages | BoardImagesGenerator] | None:
        """
        Handle the report data from the system.
        """
        raise NotImplementedError

    # Helper functions

    import builtins
    import os
    import requests
    from tqdm import tqdm
    import hashlib
    import copy
    import re
    import json
    import yaml
    import toml
    from awesomeversion import AwesomeVersion
    import urllib.parse as urllib_parse
    from src.ruyi_index_updator import config
    from src.ruyi_index_updator import util

    def load_sep_config(self) -> list:
        """
        Load all config from the matrix path
        """
        matrix_path = self.config["path"]
        res = []
        for dirpath, _, files in self.os.walk(matrix_path):
            for file_name in files:
                if file_name == "update_config.json":
                    file_path = self.os.path.join(dirpath, file_name)
                    with open(file_path, "r", encoding="utf-8") as f:
                        sep_config = self.json.load(f)
                        res.append(sep_config)
                if file_name == "update_config.yaml" or file_name == "update_config.yml":
                    file_path = self.os.path.join(dirpath, file_name)
                    with open(file_path, "r", encoding="utf-8") as f:
                        sep_config = self.yaml.safe_load(f)
                        res.append(sep_config)
                if file_name == "update_config.toml":
                    file_path = self.os.path.join(dirpath, file_name)
                    with open(file_path, "r", encoding="utf-8") as f:
                        sep_config = self.toml.load(f)
                        res.append(sep_config)
        return res

    def eval(self, source, /, globals=None, locals=None): # pylint: disable=redefined-builtin
        """
        Same as python's built-in eval, but pass locals properly
        """
        _g_a_l = self.builtins.globals()
        _g_a_l["__builtins__"] = self.builtins
        _globals = globals if globals is not None else _g_a_l
        _locals = locals if locals is not None else self.builtins.locals()
        return eval(source, globals=_globals, locals=_locals)  # pylint: disable=eval-used

    def unique_list(self, arr: list) -> list:
        """
        Unique list
        """
        a = set()
        for i in arr:
            if isinstance(i, str):
                i = i.strip()
            a.add(i)
        return list(a)

    def cmp_version(self, v1: str, v2: str) -> int:
        """
        Compare the version of two strings
        Though this function is in version_diff.py, 
        as plugins runs in a seprate env, we need to rewrite it here.
        """
        av1 = self.AwesomeVersion(v1)
        av2 = self.AwesomeVersion(v2)
        if av1 > av2:
            return 1
        if av1 < av2:
            return -1
        return 0

    def download_file(self, file: str, url: str) -> str:
        """
        Download a file from the internet url, save it to file. 
        """
        if self.os.path.exists(file):
            self.logger.info(
                "File %s already exists, skipping download.", file)
            return file
        chunk_size = 4096
        resp = self.requests.get(url, stream=True, timeout=60)
        tot_sz = int(resp.headers.get("content-length", 0))
        self.logger.info("Downloading %s to %s", url, file)
        with self.tqdm(total=tot_sz, unit="B", unit_scale=True) as pbar:
            with open(file, 'wb') as f:
                for chunk in resp.iter_content(chunk_size):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))
        return file

    def file_size(self, file: str) -> int:
        """
        Get the size of a file.
        """
        return self.os.path.getsize(file)

    def urljoin(self, base: str, path: str) -> str:
        """
        Do a urljoin
        """
        return self.urllib_parse.urljoin(base + '/', path)

    def urlbasename(self, url: str) -> str:
        """
        Get the basename of a url.
        """
        parsed = self.urllib_parse.urlparse(url)
        path = parsed.path
        if path and path.endswith('/'):
            return ""
        filename = self.os.path.basename(path)
        return filename

    def sha256sum(self, file: str) -> str:
        """
        Calculate the sha256sum of a file.
        """
        sha256 = self.hashlib.sha256()
        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                sha256.update(chunk)
        return sha256.hexdigest()

    def sha512sum(self, file: str) -> str:
        """
        Calculate the sha512sum of a file.
        """
        sha512 = self.hashlib.sha512()
        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                sha512.update(chunk)
        return sha512.hexdigest()

    def gen_distfile(self, file: str, url: str) -> DistfileDeclType:
        """
        Generate a distfile object from a file.
        """
        return {
            "name": self.os.path.basename(file),
            "size": self.file_size(file),
            "urls": [url],
            "checksums": {
                "sha256": self.sha256sum(file),
                "sha512": self.sha512sum(file),
            },
            "restrict": ["mirror"],
        }


def register() -> UploadPluginBase | None:
    """
    Register the plugin to the system
    **Required to be implemented in the plugin**
    """
    return None
