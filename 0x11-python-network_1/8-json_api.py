#!/usr/bin/python3

"""
Module for senf POST requests
"""

import requests
import sys


if __name__ == "__main__":

    try:
        val = sys.argv[1]
    except:
        val = ''

    r = requests.post(url, data={'q': val})
    url = 'http://0.0.0.0:5000/search_user'

    try:
        valid = len(r.json())
        if valid:
            d = r.json()
            print("[{}] {}".format(d["id"], d["name"]))
        else:
            print("No result")

    except:
        print("Not a valid JSON")
