#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import sys
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError

    url = sys.argv[1]
    demande = Request(url)
    try:
        with urlopen(demande) as reponse:
            print(reponse.read().decode())
    except HTTPError as error:
        print(f'Error code: {error.code}')
