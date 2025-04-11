"""
Handle the ruyi index git. Like: add a image index, upload it and make a pr etc.
"""

import os
import logging
import git
from github import Github, Auth
from github.Repository import Repository
from .config import config

logger = logging.getLogger(__name__)

CI_RUN_ID = os.getenv("CI_RUN_ID", None)
CI_RUN_URL = os.getenv("CI_RUN_URL", None)


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

<Body End>
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
                f"{self.user.login}/{config["PACKAGE_INDEX_REPO"]}")
        except:  # pylint: disable=bare-except
            ruyi_repo = self.github.get_repo(
                f"{config["PACKAGE_INDEX_OWNER"]}/{config["PACKAGE_INDEX_REPO"]}")
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

    def check_pr_updated(self, head: str, base: str) -> bool:
        """
        Check if the PR with head and base exist.
        Different from check_pr_exist, this senerio is for the PR is already exist,
        but identifier is not the same.
        Maybe the PR is manually created, or something went wrong.
        Neverthless, manual interraction is needed.
        """
        prs = self.upstream.get_pulls(state="open")
        for pr in prs:
            head_remove_user = head.split(":")[-1]
            if pr.head.ref == head_remove_user and pr.base.ref == base:
                return True
        return False
    
    def get_branch_diff(self, a: str, b: str) -> str:
        """
        Get the diff between head and base branch.
        """
        diff = self.local_repo.git.execute(
            ["git", "diff", f"{a}...{b}"],
            stdout_as_string=True
        )
        return diff

    def create_pr(self, title: str, body: str, self_branch: str, upstream_branch: str):
        """
        Create a pull request.
        """
        head = f"{self.user.login}:{self_branch}"
        base = upstream_branch
        if not config["force"] and self.check_pr_updated(head, base):
            logger.error(
                "PR already exist for %s -> %s, please check manually", head, base)
            logger.error("New PR info:")
            logger.error("Title: %s", title)
            logger.error("Body: \n%s\n<Body End>", body)
            return
        diff = self.get_branch_diff(
            "upstream/main", "HEAD"
        )
        if diff is None or len(diff) == 0 or diff == "":
            logger.info("No diff found, skip PR creation")
            return
        pr = self.upstream.create_pull(
            title=title, body=body, head=head, base=base)
        logger.info("PR created: %s at %s", pr.title, pr.html_url)

    def reset_to_upstream(self):
        """
        Reset the local repo to upstream/main.
        """
        # self.local_repo.remote().set_url(self.upstream.ssh_url)
        # self.local_repo.remote().fetch()

        # self.local_repo.remote().refs['main'].checkout()
        # self.local_repo.remote().set_url(self.repo.ssh_url)
        flag = False
        for ref in self.local_repo.remotes:
            if ref.name == "upstream":
                flag = True
                break
        if not flag:
            self.local_repo.git.execute(
                ["git", "remote", "add", "upstream", self.upstream.ssh_url]
            )

        self.local_repo.git.execute(
            ["git", "remote", "set-url", "upstream", self.upstream.ssh_url]
        )
        self.local_repo.git.execute(
            ["git", "fetch", "upstream"]
        )
        self.local_repo.git.execute(
            ["git", "reset", "--hard", "upstream/main"]
        )
        self.local_repo.git.execute(
            ["git", "clean", "-xdf"]
        )

    def clean(self):
        self.local_repo.git.execute(
            ["git", "clean", "-xdf"]
        )

    def __init__(self, repo_dir: str) -> None:
        github_token = os.getenv('GITHUB_TOKEN', None)
        if github_token is None:
            logger.error('GITHUB_TOKEN env is not set')
            raise ValueError('GITHUB_TOKEN is not set')
        auth = Auth.Token(github_token)
        self.github = Github(auth=auth)
        self.user = self.github.get_user()

        self.upstream = self.github.get_repo(
            f"{config["PACKAGE_INDEX_OWNER"]}/{config["PACKAGE_INDEX_REPO"]}")

        self.repo = self.__get_or_fork_repo()

        repo_dir = os.path.join(repo_dir, config["PACKAGE_INDEX_REPO"])

        if not os.path.exists(repo_dir):
            self.local_repo = git.Repo.clone_from(self.repo.ssh_url, repo_dir)
            logger.info("Repo cloned from %s to %s",
                        self.repo.ssh_url, repo_dir)
        else:
            self.local_repo = git.Repo(repo_dir)
            self.reset_to_upstream()
            logger.info("Repo updated to %s: %s", self.repo.ssh_url,
                        self.local_repo.head.commit)

    def local_checkout(self, branch: str):
        """
        Checkout to a branch.
        """
        self.local_repo.git.execute(
            ["git", "checkout", "main"]
        )
        for ref in self.local_repo.branches:
            if branch in ref.name:
                self.local_repo.git.branch("-D", ref.name)
        self.reset_to_upstream()
        head = self.local_repo.create_head(branch)
        head.checkout()
        self.clean()
        logger.info("Checkout to %s", branch)

    def local_add(self, file: str):
        """
        Add a file to the repo.
        """
        logger.info("Add: %s", file)
        self.local_repo.git.execute(
            ["git", "add", file]
        )

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
