#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import sys
    import requests

    repo = sys.argv[1]
    user = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(user, repo)
    response = requests.get(url)
    donnees = response.json()
    counter = 0
    for commit in donnees:
        if counter > 9:
            break
        user = commit.get("commit").get("author").get("name")
        print("{}: {}".format(commit.get("sha"), user))

        counter += 1
