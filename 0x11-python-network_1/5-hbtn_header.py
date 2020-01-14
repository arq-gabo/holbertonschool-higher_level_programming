#!/usr/bin/python3

"""
Show the value of the variable X-Request-ID
"""

import sys
import requests


if __name__ == "__main__":

    r = requests.get(sys.argv[1])
    req = r.headers.get('X-Request-Id')
    print(req)
