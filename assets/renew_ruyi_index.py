#!/usr/bin/env python3
"""
Automatically check the index of ruyi and renew it.
"""

import os
import logging

import src.ruyi_index_updator.util as util
from src.ruyi_index_updator.config import config
from src.matrix_parser import Systems
from src.ruyi_index_updator import RuyiDiff, RuyiGitRepo, RuyiGitRepoUnprivilege


def main():
    """
    Main function
    """

    logger = logging.getLogger()

    index_path = util.folder_tmp_mux(config["index"])

    matrix = Systems(config["path"])
    diffs = RuyiDiff(matrix)

    if config["unprivileged"] or os.getenv('GITHUB_TOKEN', None) is None:
        logger.error(
            "Sync tool will continue in unprivileged mode"
        )
        logger.error(
            "In unprivileged mode, all things related to remote will be skipped"
        )
        repo = RuyiGitRepoUnprivilege(index_path)
        if config["pr"]:
            logger.error("PR is not supported in unprivileged mode, bailing out")
            raise RuntimeError(
                "PR is not supported in unprivileged mode, bailing out"
            )
    else:
        repo = RuyiGitRepo(index_path)

    for worker in diffs.gen_branch(repo):
        worker.do_checkout()
        worker.do_update()
        worker.do_commit()
        worker.do_push()
        if config["pr"]:
            worker.do_pr()

    update_info = diffs.update_info()
    if config["update_info"] is not None:
        with open(config["update_info"], "w", encoding="utf-8") as f:
            f.write("|" . join([
                "", " File ", " Plug ", " Update Info ", ""
            ]))
            f.write("\n")
            f.write("|" . join([
                "", " --- ", " --- ", " --- ", ""
            ]))
            f.write("\n")
            for i in update_info:
                arr = [""] + [f" {j} " for j in i] + [""]
                f.write("|" . join(arr))
                f.write("\n")


if __name__ == '__main__':
    main()
