#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import sys
    import requests

    reponse = requests.get(sys.argv[1])
    if (reponse.status_code >= 400): # error
        print(f"Error code: {reponse.status_code}")
    else:
        print(reponse.text)
