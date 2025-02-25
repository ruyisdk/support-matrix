"""
Generate version info based on the support-matrix metadata
"""
from .matrix_parser import Systems, SystemVar


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


def gen_oldver(matrix: Systems):
    """
    Generate oldver based on the support-matrix metadata
    """
    oldver: list[VInfo] = []

    for board in matrix.boards:
        vendor = "not_defined" if board.vendor is None else board.vendor
        for system in board.systems:
            for variant in system.variant:
                variant_str = variant.sys_var if variant.sys_var is not None else 'null'
                vinfo = VInfo(vendor, system.sys, variant_str)
                vinfo.set_version(variant.sys_ver)
                vinfo.set_raw_data(variant)
                oldver.append(vinfo)

    return {
        f"{vinfo.vendor}-{vinfo.system}-{vinfo.variant}": vinfo for vinfo in oldver
    }
