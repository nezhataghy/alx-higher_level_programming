#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""


import requests

if __name__ == "__main__":
    demande = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(demande.text)}")
    print(f"\t- content: {demande.text}")
