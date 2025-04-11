"""
Structure of the board index file

See ruyi packages-index definition
"""

import os
import copy
import toml
from awesomeversion import AwesomeVersion

from ...matrix_parser import ImageStatus

from ..schema.pkg_manifest import *


class BoardImages:
    version: str
    bot_created: bool
    info: PackageManifestType

    def __init__(self, file: str | None = None, *,
                 bot_created: bool = True, version: str = None, info: PackageManifestType = None):
        if file is None:
            self.bot_created = bot_created
            self.version = version
            self.info = info
            return
        self.bot_created = False
        basename = os.path.basename(file)
        self.version = basename[:-5]  # remove .toml
        t = toml.load(file)
        self.info = t

    def __copy__(self):
        return BoardImages(bot_created=self.bot_created,
                           version=copy.copy(self.version), info=copy.copy(self.info)
                           )

    def __cmp__(self, other):
        av1 = AwesomeVersion(self.version)
        if isinstance(other, str):
            av2 = AwesomeVersion(other)
        elif isinstance(other, BoardImages):
            av2 = AwesomeVersion(other.version)
        else:
            raise NotImplementedError
        if av1 > av2:
            return 1
        if av1 < av2:
            return -1
        return 0

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __eq__(self, other):
        return self.__cmp__(other) == 0


class BoardImagesGenerator:
    def __init__(self,
                 version: str,
                 upstream_version: str,
                 desc: str,
                 vendor: str,
                 distfiles: list[DistfileDeclType],
                 strategy: str,
                 status: ImageStatus,  # Good/CFT/CFH
                 partition_map: dict[str, str]):
        self.version = version
        self.upstream_version = upstream_version
        self.desc = desc
        self.vendor = vendor
        self.distfiles = distfiles
        self.strategy = strategy
        self.status = status
        self.partition_map = partition_map

    def generate(self, version = None) -> BoardImages:
        if self.status == "good":
            level = "good"
        elif self.status == "cft":
            level = "untested"
        elif self.status == "cfh":
            level = "known_issue"
        else:
            level = None
        service_level = [{
            "level": level
        }] if level is not None else []
        info = {
            "format": "v1",
            "metadata": {
                "desc": self.desc,
                "vendor": {
                    "name": self.vendor,
                    "eula": ""
                },
                "service_level": service_level,
                "upstream_version": self.upstream_version,
            },
            "distfiles": self.distfiles,
            "blob": {
                "distfiles": [
                    dist["name"] for dist in self.distfiles
                ],
            },
            "provisionable": {
                "strategy": self.strategy,
                "partition_map": self.partition_map,
            }
        }
        return BoardImages(
            bot_created=True,
            version=version,
            info=info
        )
