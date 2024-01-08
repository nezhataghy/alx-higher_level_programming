#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import sys
    import requests

    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    donnee = {"q": letter}
    reponse = requests.post("http://0.0.0.0:5000/search_user", donnee)
    try:
        user = reponse.json()
        if not (len(user) < 1):
            print("[{}] {}".format(user["id"], user["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
