#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import sys
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode

    url = sys.argv[1]
    valeurs = {'email': sys.argv[2]}
    donnee = urlencode(valeurs)
    donnee = donnee.encode('ascii')
    demande = Request(url, donnee)

    with urlopen(demande) as reponse:
        print(reponse.read().decode())
