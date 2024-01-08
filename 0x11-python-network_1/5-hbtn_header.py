#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    reponse = requests.get(url)
    print(reponse.headers.get("X-Request-Id"))
