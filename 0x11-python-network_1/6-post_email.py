#!/usr/bin/python3

"""
Module for send a POST to request, pass tu url the parameter
and show the body of the response
"""

import sys
import requests


if __name__ == "__main__":

    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
