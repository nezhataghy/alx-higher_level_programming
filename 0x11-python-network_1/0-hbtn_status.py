#!/usr/bin/python3
"""python script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib.request import Request, urlopen
    url = "https://alx-intranet.hbtn.io/status"
    demande = Request(url)
    with urlopen(demande) as response:
        reponse = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(reponse)))
    print("\t- content: {}".format(reponse))
    print("\t- utf8 content: {}".format(reponse.decode("utf-8")))
