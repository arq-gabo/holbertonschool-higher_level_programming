#!/usr/bin/python3
"""
Module for github credentials
"""

import sys
import requests


if __name__ == "__main__":

    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    a = requests.get(url)
    count = 0
    try:
        json_data = a.json()
        for data in json_data:
            if count < 10:
                print("{}: {}".format(
                    data.get('sha'),
                    data['commit']['author'].get('name')))
                count = count + 1
    except ValueError:
        print("Not a valid JSON")
