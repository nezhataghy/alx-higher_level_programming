#!/usr/bin/python3
"""Python script thatv fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import requests

    reponse = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body reponse:")
    print("\t- type: {}".format(type(reponse.text)))
    print("\t- content: {}".format(reponse.text))
