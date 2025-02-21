#!/usr/bin/env python3
"""
Automatically check the index of ruyi and renew it.
"""

import logging

import src.ruyi_index_updator.util as util
from src.ruyi_index_updator.config import config
from src.matrix_parser import Systems
from src.ruyi_index_updator import RuyiDiff, RuyiGitRepo


def main():
    """
    Main function
    """

    logger = logging.getLogger()

    index_path = util.folder_tmp_mux(config["index"])

    matrix = Systems(config["path"])
    diffs = RuyiDiff(matrix)
    repo = RuyiGitRepo(index_path)

    for branch in diffs.gen_branch():
        pr = repo.push(branch)
        if pr is None:
            continue
        if not config["pr"]:
            logger.info("%s", repr(pr))
            continue
        if config["force"]:
            pr.title = f"[Force Update] {pr.title}"
        repo.create_wrapped_pr(pr)

    update_info = diffs.update_info()
    if config["update_info"] is not None:
        with open(config["update_info"], "w", encoding="utf-8") as f:
            f.write("|" . join([
                "", "File", "Triple", "Update Info", ""
            ]))
            f.write("\n")
            f.write("|" . join([
                "", "---", "---", "---", ""
            ]))
            f.write("\n")
            for i in update_info:
                f.write("|" . join([
                    "", i[0], i[1], i[2], ""
                ]))
                f.write("\n")

if __name__ == '__main__':
    main()
