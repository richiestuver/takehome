import sys
from os import getenv

from dotenv import load_dotenv
from github import Github
from github import Auth


def get_cli_inputs() -> list[str]:
    return sys.argv[1:]


def init_github() -> Github:
    load_dotenv()
    token = getenv("GITHUB_TOKEN", "")
    auth = Auth.Token(token)
    return Github(auth=auth)


if __name__ == "__main__":
    github = init_github()
    repo_names = get_cli_inputs()

    users = set()
    for name in repo_names:
        repo = github.get_repo(name)
        stargazers = repo.get_stargazers()
        users |= set([user.login for user in stargazers])

    print("\n".join(users))
