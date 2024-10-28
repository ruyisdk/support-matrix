"""
Generate oldver based on the support-matrix metadata
"""

import toml
from ..matrix_parser import Systems, SystemVar


class VInfo:
    """
    Version info of a system, compare version using awesomeversion plz
    """
    vendor: str
    system: str
    variant: str
    version: str | None
    raw_data: SystemVar | None

    def __init__(self, vendor: str, system: str, variant: str):
        self.vendor = vendor
        self.system = system
        self.variant = variant
        self.version = None

    def __eq__(self, value: object) -> bool:
        if isinstance(value, VInfo):
            return self.vendor == value.vendor and \
                self.system == value.system and self.variant == value.variant
        if isinstance(value, str):
            vendor, system, variant = value.split('-')
            return self.vendor == vendor and self.system == system and self.variant == variant
        if isinstance(value, tuple) and len(value) == 3:
            vendor, system, variant = value
            return self.vendor == vendor and self.system == system and self.variant == variant
        return False

    def set_version(self, version: str):
        """
        Set the version of the system
        """
        self.version = version

    def set_raw_data(self, raw_data: SystemVar):
        """
        Set the raw data of the system
        """
        self.raw_data = raw_data

    def __repr__(self) -> str:
        return f"{self.vendor}-{self.system}-{self.variant}: {self.version}"


def vinfo_list_to_dict(vinfo: list[VInfo]) -> dict[str, dict[str, str]]:
    """
    Convert VInfo to dict
    """
    return {
        f"{vinfo.vendor}-{vinfo.system}-{vinfo.variant}": {
            "version": vinfo.version
        } for vinfo in vinfo
    }


def vinfo_list_to_vinfo_dict(vinfo: list[VInfo]) -> dict[str, VInfo]:
    """
    Convert VInfo to dict
    """
    return {
        f"{vinfo.vendor}-{vinfo.system}-{vinfo.variant}": vinfo for vinfo in vinfo
    }


def vinfo_dict_to_dict(vinfo: dict[str, VInfo]) -> dict[str, dict[str, str]]:
    """
    Convert VInfo to dict
    """
    return {
        f"{vinfo.vendor}-{vinfo.system}-{vinfo.variant}": {
            "version": vinfo.version
        } for vinfo in vinfo.values()
    }


def gen_oldver(matrix: Systems, nvchecker_conf: str):
    """
    Generate oldver based on the support-matrix metadata
    """
    nv_conf = toml.load(nvchecker_conf)
    if '__config__' in nv_conf.keys():
        del nv_conf['__config__']
    oldver: list[VInfo] = []

    for prod, _ in nv_conf.items():
        if prod in oldver:
            continue
        prod_s = prod.split('-')
        if len(prod_s) != 3:
            continue
        vendor, system, variant = prod_s
        oldver.append(VInfo(vendor, system, variant))

    for board in matrix.boards:
        if board.vendor is None:
            continue
        for system in board.systems:
            for variant in system.variant:
                prod = f"{board.vendor}-{variant.sys}-"\
                    f"{variant.sys_var if variant.sys_var is not None else 'null'}"
                if prod not in oldver:
                    continue
                for vinfo in oldver:
                    if vinfo == prod:
                        vinfo.set_version(variant.sys_ver)
                        vinfo.set_raw_data(variant)
                        break

    return vinfo_list_to_vinfo_dict(oldver)
