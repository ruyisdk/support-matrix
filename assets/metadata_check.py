import os
import logging
import datetime
import argparse
from typing import Annotated, Optional
import yaml


from pydantic import BaseModel, AfterValidator, field_validator

from src.matrix_parser import Systems, ImageStatus

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', dest="path",
                    help="support matrix path", type=str, default='.')
args = parser.parse_args()


class BoardMetadata(BaseModel):
    """
    BoardMetadata
    """

    product: str
    cpu: str
    cpu_core: str
    ram: str

    vendor: Optional[str] = None
    board_variants: Optional[list[str]] = None

    @field_validator('vendor', mode='before')
    @classmethod
    def check_vendor(cls, v):
        """
        check_vendor
        """
        if v is not None and \
            not all(c.isalnum() or c in '_-' for c in v):
            raise ValueError(f"Invalid vendor name: {v}.")
        return v


def status_validator(v: str):
    """
    status_validator
    """
    mapper = ImageStatus.MAPPER
    if v.lower() not in mapper:
        raise ValueError(f"Invalid status: {v}.")
    return v


StatusValidator = Annotated[str, AfterValidator(status_validator)]

AllowSystemTypes = [
    'linux',
    'bsd',
    'rtos',
    'others',
    'customized',
]


def system_validator_generator():
    """
    system_validator
    """
    meta_path = os.path.join(args.path, 'assets', 'metadata.yml')
    with open(meta_path, 'r', encoding="utf-8") as f:
        meta = yaml.safe_load(f)
    support_systems = []
    for k, v in meta.items():
        if k not in AllowSystemTypes:
            raise ValueError(f"Invalid system type: {k}.")
        for pq in v:
            if len(pq) == 0:
                raise ValueError(f"Invalid system name: {pq}.")
            if len(pq) > 1:
                raise ValueError(f"Invalid system name: {pq}.")

            for p, _ in pq.items():
                # Check the key should only contains alphanumeric and underscore
                if not all(c.isalnum() or c in '_-' for c in p):
                    raise ValueError(f"Invalid system name: {p}.")
                support_systems.append(p.lower())

    def system_validator_fn(v: str):
        """
        system_validator
        """
        if v.lower() not in support_systems:
            raise ValueError(f"Invalid system name: {v}.")
        return v
    return system_validator_fn


system_validator = system_validator_generator()
SystemValidator = Annotated[str, AfterValidator(system_validator)]


class SystemMetadata(BaseModel):
    """
    SystemMetadata
    """

    sys: SystemValidator
    sys_ver: str | None
    sys_var: str | None
    status: StatusValidator
    last_update: datetime.datetime


matrix = Systems(args.path)
for board in matrix.boards:
    if not hasattr(board, 'raw_data'):
        continue
    logger.info("Checking board: %s", board.link)
    board_raw = board.raw_data
    board_frontmatter = board_raw.metadata
    board_metadata = BoardMetadata(**board_frontmatter)

    for sys in board.systems:
        # Check whether sys_var is distinct
        existing_sys_vars = set()
        for var in sys.variant:
            if not hasattr(var, 'raw_data'):
                continue
            logger.info("Checking system: %s", var.link)
            sys_raw = var.raw_data
            sys_frontmatter = sys_raw.metadata
            sys_metadata = SystemMetadata(**sys_raw)
            if sys_metadata.sys_var in existing_sys_vars:
                raise ValueError(
                    f"Duplicate system variant: {sys_metadata.sys_var}.")
            existing_sys_vars.add(sys_metadata.sys_var)
