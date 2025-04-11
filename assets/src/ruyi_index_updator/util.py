"""
Utils
"""

import atexit
import tempfile
import shutil

from awesomeversion import AwesomeVersion
from awesomeversion.typing import AwesomeVersionStrategy

from ..matrix_parser import SystemInfo, SystemIdentifier


def folder_tmp_mux(folder: str | None) -> str:
    """
    If the folder is None, return a tmp folder.

    Clean the tmp folder if created.

    A special usage is to use it as a automatiaclly clean tmp folder **after** the program ends,
    as tmpfile only gives this ability in the context manager.
    """
    p = folder if folder is not None else tempfile.mkdtemp()

    def __release_tmp_path():
        shutil.rmtree(p)
    if folder is None:
        atexit.register(__release_tmp_path)
    return p


def cmp_version(ver1: str, ver2: str) -> int:
    """
    Compare the version
    """
    av1 = AwesomeVersion(ver1, ensure_strategy=AwesomeVersionStrategy.SEMVER)
    av2 = AwesomeVersion(ver2, ensure_strategy=AwesomeVersionStrategy.SEMVER)
    if av1 > av2:
        return 1
    if av1 < av2:
        return -1
    return 0


def remove_file_extension(name: str) -> str:
    """
    Remove the last part of a file name, only works for compressed files.
    eg: a.img.zstd -> a.img
    """
    compressed_exts = ['zstd', 'xz', 'gz', 'bz2', 'lzma', 'lz4', 'lzo', 'z', '7z', 'zip']
    for ext in compressed_exts:
        if name.endswith(f".{ext}"):
            return '.'.join(name.split('.')[:-1])
    return name


def board_id(info: SystemInfo | SystemIdentifier) -> str:
    """
    Return the board id
    """
    return info.vendor


def board_variants(info: SystemInfo | SystemIdentifier) -> list[str]:
    """
    Return the board variants
    """
    if info.board_variants is None:
        return ['generic']
    return info.board_variants


def system_id(info: SystemInfo | SystemIdentifier, board_variant: str | None) -> str:
    """
    Return the system id
    """
    # This map should be removed.
    # But some changes in packages-index is needed.
    # So we need to keep it for now.
    system = info.system
    if system == 'openeuler':
        system = 'oerv'
    if system == 'buildroot':
        system = 'buildroot-sdk'

    system_vendor = info.vendor

    if info.variant is None or info.variant == '':
        system_variant = ''
    else:
        system_variant = f"-{info.variant}"

    if board_variant is None or board_variant == 'generic':
        board_variant = ''
    else:
        board_variant = f"-{board_variant}"

    return f"{system}-{system_vendor}{board_variant}{system_variant}"


def file_id(info: SystemInfo | SystemIdentifier,
            board_variant: str | None, file_prepend: str | None, file_append: str | None = None) -> str:
    """
    Return the file id
    """
    # This map should be removed.
    # But some changes in packages-index is needed.
    # So we need to keep it for now.
    sys_id = system_id(info, board_variant)

    if file_prepend is None or file_prepend == '':
        prepend = ''
    else:
        prepend = f"{file_prepend}-"
    if file_append is None or file_append == '':
        append = ''
    else:
        append = f"{file_append}-"

    return f"{prepend}{sys_id}{append}"
