#!/bin/python
"""Entry point for fzf-launcher."""
import sys
from subprocess import run, PIPE

chrome_mahi = "google-chrome-mahi"
chrome_personal = "google-chrome-personal"


def bitbucket_branches(repo) -> str:
    return f"https://bitbucket.org/viewspark/viewspark-{repo}/branches/"


def bitbucket_prs(repo) -> str:
    return f"https://bitbucket.org/viewspark/viewspark-{repo}/pull-requests/"


vs_repos = [
    "admin-android", "admin-service", "admin-web", "auth-service",
    "backend-common", "charity-json", "db-android", "db-ios",
    "delivery-service", "deploy-data", "donor-web", "firebase", "gen-tools",
    "media-service", "notification-service", "onboarding-scripts",
    "payment-service", "publish-service", "search-service", "test-harness"
]

vs_bitbucket = {
    f"bitbucket-viewspark-{repo}": f"{chrome_mahi} {bitbucket_branches(repo)}"
    for repo in vs_repos
}

vs_bitbucket_prs = {
    f"bitbucket-pr-viewspark-{repo}": f"{chrome_mahi} {bitbucket_prs(repo)}"
    for repo in vs_repos
}

commands = {
    "online-go": f"{chrome_personal} online-go.com",
    **vs_bitbucket_prs,
    **vs_bitbucket
}


def tags() -> str:
    options = "\n".join(list(commands.keys()))
    return options


def less_convoluted() -> None:
    if "--wrapper" in sys.argv:
        run(
            "alacritty --class=Alacritty,FloatingAlacritty -e "
            "python ~/Projects/fzf-launcher/fzf_launcher.py & disown",
            shell=True)
        return

    c = run(f"echo \"{tags()}\" | fzf", shell=True, stdin=PIPE, stdout=PIPE)
    tag = c.stdout.decode().strip()
    if tag != "":
        run(commands[tag], shell=True)


if __name__ == "__main__":
    less_convoluted()
