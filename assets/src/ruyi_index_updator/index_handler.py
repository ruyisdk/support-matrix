"""
Handle the ruyi index git. Like: add a image index, upload it and make a pr etc.
"""

import os
import logging
import git
from github import Github, Auth
from github.Repository import Repository
from .version_diff import BoardImageWrapper

logger = logging.getLogger(__name__)

PACKAGE_INDEX_OWNER = "ruyisdk"
PACKAGE_INDEX_REPO = "packages-index"


class PrWrapper:
    """
    A wrapper for pull request info.
    """

    def __init__(self, title: str, body: str, self_branch: str, upstream_branch: str) -> None:
        self.title = title
        self.body = body
        self.self_branch = self_branch
        self.upstream_branch = upstream_branch

    def __repr__(self) -> str:
        return f"""\
PR:
    Title: {self.title}
    Body: 
{self.body} 

    From: {self.self_branch}
    To: {self.upstream_branch}
"""


class RuyiGitRepo:
    """
    Your Github index repo.
    """

    def __get_or_fork_repo(self) -> Repository:
        # We assert the PACKAGE_INDEX_REPO is the ruyi index repo.
        try:
            repo = self.github.get_repo(
                f"{self.user.login}/{PACKAGE_INDEX_REPO}")
        except:  # pylint: disable=bare-except
            ruyi_repo = self.github.get_repo(
                f"{PACKAGE_INDEX_OWNER}/{PACKAGE_INDEX_REPO}")
            repo = self.user.create_fork(repo=ruyi_repo)
        return repo

    def check_pr_exist(self, identifer: str) -> bool:
        """
        Check if the PR with identifer exist.

        The identifer is the hash of the image index. In the PR body, it should be like:
        [HASH[<hash>]]
        """
        prs = self.upstream.get_pulls(state="open")
        for pr in prs:
            if pr.body is not None\
                    and f"[HASH[{identifer}]]" in pr.body:
                return True
        return False

    def __create_pr(self, wrapper: PrWrapper):
        """
        Create a pull request.
        """
        head = f"{self.user.login}:{wrapper.self_branch}"
        pr = self.upstream.create_pull(
            title=wrapper.title, body=wrapper.body, head=head, base=wrapper.upstream_branch)
        logger.info("PR created: %s at %s", pr.title, pr.html_url)

    def create_wrapped_pr(self, wrapper: PrWrapper):
        """
        Create a pull request.
        """
        self.__create_pr(wrapper)

    def create_pr(self, title: str, body: str, self_branch: str, upstream_branch: str):
        """
        Create a pull request.
        """
        self.__create_pr(PrWrapper(
            title, body, self_branch, upstream_branch))

    def __reset_to_upstream(self):
        self.local_repo.remote().set_url(self.upstream.ssh_url)
        self.local_repo.remote().fetch()

        self.local_repo.remote().refs['main'].checkout()
        self.local_repo.remote().set_url(self.repo.ssh_url)

    def __init__(self, repo_dir: str) -> None:
        github_token = os.getenv('GITHUB_TOKEN', None)
        if github_token is None:
            logger.error('GITHUB_TOKEN env is not set')
            raise ValueError('GITHUB_TOKEN is not set')
        auth = Auth.Token(github_token)
        self.github = Github(auth=auth)
        self.user = self.github.get_user()

        self.upstream = self.github.get_repo(
            f"{PACKAGE_INDEX_OWNER}/{PACKAGE_INDEX_REPO}")

        self.repo = self.__get_or_fork_repo()

        repo_dir = os.path.join(repo_dir, PACKAGE_INDEX_REPO)

        if not os.path.exists(repo_dir):
            self.local_repo = git.Repo.clone_from(self.repo.ssh_url, repo_dir)
            logger.info("Repo cloned from %s to %s",
                        self.repo.ssh_url, repo_dir)
        else:
            self.local_repo = git.Repo(repo_dir)
            self.__reset_to_upstream()
            logger.info("Repo updated to %s: %s", self.repo.ssh_url,
                        self.local_repo.head.commit)

    def local_checkout(self, branch: str):
        """
        Checkout to a branch.
        """
        for ref in self.local_repo.branches:
            if branch in ref.name:
                self.local_repo.git.branch("-D", ref.name)
        self.__reset_to_upstream()
        head = self.local_repo.create_head(branch)
        head.checkout()
        logger.info("Checkout to %s", branch)

    def local_commit(self, message: str):
        """
        Commit the changes.
        """
        logger.info("Commit: %s", message)
        message = f"{message}\n\nThis commit is made by ruyi-index-updator"
        self.local_repo.index.commit(message)

    def local_push(self, branch: str):
        """
        Push the changes to remote.
        """
        logger.info("Push to remote: %s", self.local_repo.remote().url)
        # This won't set remote branch if it doesn't exist
        # self.local_repo.remote().push(refspec=f"{branch}:{branch}")
        self.local_repo.git.execute(
            ["git", "push", "--set-upstream", "origin", branch, "-f"]
        )

    def add_image(self, image: BoardImageWrapper):
        """
        Add a image index to the repo.
        """
        index_name = image.new_index_name()
        index_file = os.path.join(
            self.local_repo.working_dir,
            "manifests",
            "board-image",
            index_name
        )
        with open(index_file, "w", encoding="utf-8") as f:
            f.write(image.new_index_toml())
        self.local_repo.index.add([index_file])
        logger.info("Add %s", index_name)

    def upload_image(self, image: BoardImageWrapper):
        """
        Upload the image index to the repo.
        """

        if self.check_pr_exist(image.gen_hash()):
            logger.info("PR for %s already exist, skip", image.index_name)
            return

        branch_name = f"{image.index_name}-{image.index.raw_version}"
        self.local_checkout(branch_name)
        self.add_image(image)
        message = f"board-image/{image.index_name}:"\
            f" Bump to {image.index.version}"
        body = f"""\
Bump {image.index_name} from {image.old_indexs[-1].version} to {image.index.version}.

Identifier: [HASH[{image.gen_hash()}]]

This PR is made by ruyi-index-updator bot.
"""
        self.local_commit(message)
        self.local_push(branch_name)
        return PrWrapper(
            title=message,
            body=body,
            self_branch=branch_name,
            upstream_branch="main"
        )
