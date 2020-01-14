#!/usr/bin/python3

"""
Module for show the request
"""

import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import urllib.error

if __name__ == "__main__":

    url = sys.argv[1]

    try:
        req = Request(url)
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
