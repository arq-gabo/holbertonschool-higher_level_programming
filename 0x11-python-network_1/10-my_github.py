#!/usr/bin/python3

"""
Python script that takes your Github credentials
(username and password) and uses the Github API
to display your id
"""

import sys
import requests


if __name__ == "__main__":

    url = "https://api.github.com/users/"
    users = sys.argv[1]
    passw = sys.argv[2]
    r = requests.get(url, auth=(users, passw))
    d = r.json()
    print(d.get('id'))
