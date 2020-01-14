#!/usr/bin/python3

"""
Module for show the Request ID
"""

import sys
from urllib.request import urlopen


if __name__ == "__main__":


    url = sys.argv[1]
    with urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
