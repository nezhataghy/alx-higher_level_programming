#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    email = sys.argv[2]
    donnee = {"email": email}
    dmnd = requests.post(url, donnee)
    print(dmnd.text)
