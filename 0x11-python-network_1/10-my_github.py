#!/usr/bin/python3

"""
Python script that takes your Github credentials
(username and password) and uses the Github API
to display your id
"""

import sys
import requests


if __name__ == "__main__":

    users = sys.argv[1]
    passw = sys.argv[2]
    url = "https://api.github.com/users/{}".format(users)
    r = requests.get(url, auth=(users, passw))
    d = r.json()
    print(d.get("id"))
