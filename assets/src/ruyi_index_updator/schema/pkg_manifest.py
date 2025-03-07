"""
Notice:
    This file comes from repo `ruyisdk/ruyi` `ruyi/ruyipkg/pkg_manifest.py`

    Version: 0.28.0

    LICENSE: Apache-2.0
"""

from copy import deepcopy
from functools import cached_property
import json
import os
import pathlib
import re
import sys
from typing import (
    Any,
    BinaryIO,
    Final,
    Iterable,
    Iterator,
    Literal,
    TypedDict,
    TYPE_CHECKING,
    cast,
)

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

from typing_extensions import NotRequired, Self

class VendorDeclType(TypedDict):
    name: str
    eula: str | None


RestrictKind = Literal["fetch"] | Literal["mirror"]


class FetchRestrictionDeclType(TypedDict):
    msgid: str
    params: "NotRequired[dict[str, str]]"


class DistfileDeclType(TypedDict):
    name: str
    urls: "NotRequired[list[str]]"
    restrict: "NotRequired[list[RestrictKind]]"
    size: int
    checksums: dict[str, str]
    strip_components: "NotRequired[int]"
    unpack: "NotRequired[UnpackMethod]"
    fetch_restriction: "NotRequired[FetchRestrictionDeclType]"


class BinaryFileDeclType(TypedDict):
    host: str
    distfiles: list[str]


BinaryDeclType = list[BinaryFileDeclType]


class BlobDeclType(TypedDict):
    distfiles: list[str]


class SourceDeclType(TypedDict):
    distfiles: list[str]


class ToolchainComponentDeclType(TypedDict):
    name: str
    version: str


class ToolchainDeclType(TypedDict):
    target: str
    flavors: list[str]
    components: list[ToolchainComponentDeclType]
    included_sysroot: "NotRequired[str]"


EmulatorFlavor = Literal["qemu-linux-user"]


class EmulatorProgramDeclType(TypedDict):
    path: str
    flavor: EmulatorFlavor
    supported_arches: list[str]
    binfmt_misc: "NotRequired[str]"


class EmulatorDeclType(TypedDict):
    flavors: "NotRequired[list[str]]"
    programs: list[EmulatorProgramDeclType]


PartitionKind = (
    Literal["boot"]
    | Literal["disk"]
    | Literal["live"]
    | Literal["root"]
    | Literal["uboot"]
)

# error: "<typing special form>" has no attribute "__args__"
# KNOWN_PARTITION_KINDS = frozenset(kind.__args__[0] for kind in PartitionKind.__args__)
KNOWN_PARTITION_KINDS: Final = frozenset(("boot", "disk", "live", "root", "uboot"))

PartitionMapDecl = dict[PartitionKind, str]


class ProvisionableDeclType(TypedDict):
    partition_map: PartitionMapDecl
    strategy: str


PackageKind = (
    Literal["binary"]
    | Literal["blob"]
    | Literal["source"]
    | Literal["toolchain"]
    | Literal["emulator"]
    | Literal["provisionable"]
)

ALL_PACKAGE_KINDS: Final[list[PackageKind]] = [
    "binary",
    "blob",
    "source",
    "toolchain",
    "emulator",
    "provisionable",
]

RuyiPkgFormat = Literal["v1"]

ServiceLevelKind = Literal["known_issue"] | Literal["untested"]

ALL_SERVICE_LEVEL_KINDS: Final[list[ServiceLevelKind]] = ["known_issue", "untested"]


class ServiceLevelDeclType(TypedDict):
    level: ServiceLevelKind
    msgid: "NotRequired[str]"
    params: "NotRequired[dict[str, str]]"


class PackageMetadataDeclType(TypedDict):
    slug: "NotRequired[str]"  # deprecated for v1+
    desc: str
    doc_uri: "NotRequired[str]"
    vendor: VendorDeclType
    service_level: "NotRequired[list[ServiceLevelDeclType]]"


class InputPackageManifestType(TypedDict):
    format: "NotRequired[RuyiPkgFormat]"

    # v0 fields
    slug: "NotRequired[str]"
    kind: "NotRequired[list[PackageKind]]"  # mandatory in v0
    desc: "NotRequired[str]"  # mandatory in v0
    doc_uri: "NotRequired[str]"
    vendor: "NotRequired[VendorDeclType]"  # mandatory in v0

    # v1+ fields
    metadata: "NotRequired[PackageMetadataDeclType]"

    # common fields
    distfiles: list[DistfileDeclType]
    binary: "NotRequired[BinaryDeclType]"
    blob: "NotRequired[BlobDeclType]"
    source: "NotRequired[SourceDeclType]"
    toolchain: "NotRequired[ToolchainDeclType]"
    emulator: "NotRequired[EmulatorDeclType]"
    provisionable: "NotRequired[ProvisionableDeclType]"


class PackageManifestType(TypedDict):
    format: RuyiPkgFormat
    kind: list[PackageKind]
    metadata: PackageMetadataDeclType
    distfiles: list[DistfileDeclType]
    binary: "NotRequired[BinaryDeclType]"
    blob: "NotRequired[BlobDeclType]"
    source: "NotRequired[SourceDeclType]"
    toolchain: "NotRequired[ToolchainDeclType]"
    emulator: "NotRequired[EmulatorDeclType]"
    provisionable: "NotRequired[ProvisionableDeclType]"

