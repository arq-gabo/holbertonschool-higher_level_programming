#!/usr/bin/python3

"""
Module State whit request
"""


import requests

if __name__ == "__main__":

    r = requests.get('https://intranet.hbtn.io/status')
    req = r.text
    print("Body response:")
    print("\t- type: {}".format(type(req)))
    print("\t- content: {}".format(req))
