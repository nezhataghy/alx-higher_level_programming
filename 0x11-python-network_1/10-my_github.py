#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import sys
    import requests

    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    reponse = requests.get(url, auth=(username, password))
    try:
        print(reponse.json()["id"])
    except KeyError:
        print("None")
