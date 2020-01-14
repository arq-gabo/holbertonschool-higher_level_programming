#!/usr/bin/python3

"""
Module por show email
"""


import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode

if __name__ == "__main__":

    url = sys.argv[1]
    data = urlencode({"email": sys.argv[2]}).encode('utf-8')

    req = Request(url, data)
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
