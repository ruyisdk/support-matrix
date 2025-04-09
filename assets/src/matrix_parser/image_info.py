"""
Generate version info based on the support-matrix metadata
"""
from .matrix_parser import Board, System, Systems, SystemVar


class SystemInfo:
    """
    Info of a system

    Structure:
    Due to image file is not consider in the report, It only define the three level of the system
    ```
    Device as vendor (eg: LicheePi-4A as sipeed-lpi4a)
        |
        |--- Board Variants as board_var (eg: 4g ver as 4g)
        |       |
        |       |--- System Variant as {sys}(_{sys_var})? (eg: RevyOS as revyos)
        |       |       |
        |       |       |--- File as file (eg: uboot as uboot)
        |       |       |
        |       |       |--- File (eg: boot)
        |       |       |
        |       |       |--- File (eg: root)
        |       |
        |       |--- System Variant (eg: openKylin)
        |               |
        |               |--- File (eg: uboot)
        |               |
        |               |--- File (eg: boot)
        |               |
        |               |--- File (eg: root)
        |
        |--- Board Variants (eg: 8g ver)
                |
                |--- System Variant (eg: RevyOS)
                |       |
                |       |--- File (eg: uboot)
                |       |
                |       |--- File (eg: boot)
                |       |
                |       |--- File (eg: root)
                |
                |--- System Variant (eg: openKylin)
                        |
                        |--- File (eg: uboot)
                        |
                        |--- File (eg: boot)
                        |
                        |--- File (eg: root)
    ```
    """
    product: str
    vendor: str | None
    board_variants: list[str] | None

    system: str
    variant: str | None

    version: str | None
    raw_data: SystemVar | None

    def __init__(self, board: Board, system: System, variant: SystemVar):
        self.product = board.product
        self.vendor = board.vendor
        self.board_variants = board.board_variants

        self.system = system.sys
        self.variant = variant.sys_var
        self.version = variant.sys_ver
        self.raw_data = variant

        if self.board_variants is None:
            self.board_variants = ["generic"]

    def __eq__(self, value: object) -> bool:
        if isinstance(value, SystemInfo):
            variant = value.variant if value.variant != "null" else None
            return self.vendor == value.vendor and \
                self.system == value.system and self.variant == variant
        if isinstance(value, SystemIdentifier):
            variant = value.variant if value.variant != "null" else None
            return self.vendor == value.vendor and \
                self.system == value.system and self.variant == variant
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
        return f"<SystemInfo: {self.vendor or 'no_vendor'}-{self.system}-{self.variant or 'no_variant'}: {self.version}>"


def gen_oldver(matrix: Systems) -> list[SystemInfo]:
    """
    Generate oldver based on the support-matrix metadata
    """
    oldver: list[SystemInfo] = []

    for board in matrix.boards:
        for system in board.systems:
            for variant in system.variant:
                info = SystemInfo(board, system, variant)
                oldver.append(info)

    return oldver


class SystemIdentifier:
    """
    Identifier of a system

    So the SystemInfo need something to be compared with, i.e. PartialEq

    If generate a dummy class to compare, it will be a little bit complex
    So we need a class to identify the system
    """
    vendor: str | None

    board_variant: str | None

    system: str
    variant: str | None

    def __init__(self, vendor: str | None, system: str, variant: str | None):
        self.vendor = vendor
        self.system = system
        self.variant = variant
