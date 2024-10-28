"""
Automatically check the index of ruyi and renew it.
"""

import shutil
import argparse
import tempfile
import logging
import colorlog

from src.matrix_parser import Systems
from src.ruyi_index_updator import RuyiDiff, RuyiGitRepo

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s[%(relativeCreated)d %(levelname)s]%(reset)s: %(message)s'))

logging.basicConfig(level=logging.INFO, handlers=[handler])

logger = logging.getLogger(__name__)


def main():
    """
    Main function
    """

    arg = argparse.ArgumentParser()
    arg.add_argument('-c', '--config', help='config file',
                     default='assets/config.toml')
    arg.add_argument(
        '-p', '--path', help='path to the support matrix', default='.')
    arg.add_argument(
        '-i', '--index', help='path clone of ruyi index, default to a temp dir', default=None
    )
    arg.add_argument(
        '--pr', help='create a PR for the update', action='store_true'
    )
    args = arg.parse_args()

    index_path = args.index
    if index_path is None:
        index_path = tempfile.mkdtemp()

    matrix = Systems(args.path)
    diffs = RuyiDiff(matrix, args.config)
    repo = RuyiGitRepo(index_path)

    for diff in diffs.gen_diff():
        pr = repo.upload_image(diff)
        if pr is None:
            continue
        if not args.pr:
            logger.info("""\
PR info:
    Title: %s

    Body: 
%s
    <Body End>
    Branch: %s -> upstream/%s
""", pr.title, pr.body, pr.self_branch, pr.upstream_branch)
            continue
        repo.create_wrapped_pr(pr)

    if args.index is None:
        shutil.rmtree(index_path)


if __name__ == '__main__':
    main()
