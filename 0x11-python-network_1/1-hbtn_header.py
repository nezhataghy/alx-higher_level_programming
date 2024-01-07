#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import sys
    from urllib.request import Request, urlopen
    url = sys.argv[1]
    demande = Request(url)
    with urlopen(demande) as response:
        reponse = response.getheaders()

    for header in reponse:
        if header[0] == "X-Request-Id":
            print(header[1])

    # with urllib.request.urlopen(url) as response:
    #   print(response.headers.get('X-Request-Id'))
