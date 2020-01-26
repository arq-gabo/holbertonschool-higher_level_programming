#!/usr/bin/python3
"""
Module for github credentials
"""

import sys
import requests



if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1]
    )
    r = requests.get(url)
    counter = 0
    try:
        json_data = r.json()
        for data in json_data:
            if counter < 10:
                print("{}: {}".format(
                    data.get('sha'),
                    data['commit']['author'].get('name'))
                  )
                counter = counter + 1
    except ValueError:
        print("Not a valid JSON")
