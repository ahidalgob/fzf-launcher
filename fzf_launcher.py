import sys

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


def print_tags() -> None:
    options = "\n".join(list(commands.keys()))
    print(options)


def convoluted() -> None:
    if len(sys.argv) == 1:
        print_tags()
    else:
        print(commands[sys.argv[1]])


if __name__ == "__main__":
    convoluted()
