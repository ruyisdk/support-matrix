"""
Notice:
    This file comes from repo `ruyisdk/ruyi` `ruyi/ruyipkg/pkg_manifest.py`

    Version: 0.28.0

    LICENSE: Apache-2.0
"""

from typing import Literal, TypeAlias, TypedDict, TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import NotRequired


class ImageComboDecl(TypedDict):
    id: str
    display_name: str
    packages: list[str]
    postinst_msgid: "NotRequired[str]"


class DeviceVariantDecl(TypedDict):
    id: str
    display_name: str
    supported_combos: list[str]


class DeviceDecl(TypedDict):
    id: str
    display_name: str
    variants: list[DeviceVariantDecl]


ProvisionerConfigVersion: TypeAlias = Literal["v1"]


class ProvisionerConfig(TypedDict):
    ruyi_provisioner_config: ProvisionerConfigVersion
    devices: list[DeviceDecl]
    image_combos: list[ImageComboDecl]
    postinst_messages: "NotRequired[dict[str, str]]"
