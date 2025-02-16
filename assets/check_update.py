"""
Check for updates in the matrix
"""

import sys
import argparse
import logging
from src.matrix_parser import Systems, gen_oldver
from src.version_checker import run_nvchecker, filter_newer

logger = logging.getLogger(__name__)

def main():
    """
    Main function
    """

    arg = argparse.ArgumentParser()
    arg.add_argument('-c', '--config', help='config file',
                     default='config.toml')
    arg.add_argument(
        '-p', '--path', help='path to the support matrix', default='../')
    args = arg.parse_args()

    matrix = Systems(args.path)
    old = gen_oldver(matrix)

    new, fail = run_nvchecker(oldvers=old)
    if fail:
        logger.exception("Failed to run nvchecker: %s", fail)
        sys.exit(-1)
    old = {
        f"{vinfo.vendor}-{vinfo.system}-{vinfo.variant}": {
            "version": vinfo.version
        } for vinfo in old.values()
    }

    upd = filter_newer(old, new)

    has_update = False
    for prod, ver in upd.items():
        if ver['old'] is None:
            logger.info(
                "Found new version for %s: %s", prod, ver['new']['version'])
            has_update = True
        elif ver['new'] is None:
            logger.info(
                "No new version found for %s", prod)
        else:
            logger.info(
                "Can be updated for %s: %s -> %s",
                prod, ver['old']['version'], ver['new']['version'])
            has_update = True

    if has_update:
        logger.info("Update available")


if __name__ == '__main__':
    main()
