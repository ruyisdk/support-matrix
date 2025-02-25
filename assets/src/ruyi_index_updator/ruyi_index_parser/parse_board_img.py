"""
Structure of the board index file

See ruyi packages-index definition
"""

from ..schema.pkg_manifest import *
import os
import copy
import toml
from awesomeversion import AwesomeVersion


class BoardImages:
    """
    Hold one version of the board image index
    """
    raw_version: str
    is_bot_created: bool
    info: PackageManifestType

    @property
    def version(self) -> str:
        """
        return the version
        """
        return self.raw_version

    @version.setter
    def version(self, value: str):
        self.raw_version = value

    def __init__(self, file: str | None = None, *,
                 bot_created: bool = True, version: str = None, info: PackageManifestType = None):
        if file is None:
            self.is_bot_created = bot_created
            self.raw_version = version
            self.info = info
            return
        self.is_bot_created = False
        basename = os.path.basename(file)
        self.version = basename[:-5]  # remove .toml
        t = toml.load(file)
        self.info = t

    def serialize(self) -> dict:
        """
        Serialize
        """
        return self.info

    def __copy__(self):
        return BoardImages(bot_created=False,
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
