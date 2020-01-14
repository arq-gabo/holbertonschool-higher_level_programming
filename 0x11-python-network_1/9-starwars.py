#!/usr/bin/python3

"""
Module takes in a string and sends a search request to the Star Wars
"""


import requests
import sys


if __name__ == "__main__":


    url = 'https://swapi.co/api/people/'

    sw = {"search": sys.argv[1]}
    r = requests.get(url, params=sw)
    d = r.json()
    print("Number of results: {}".format(d["count"]))
    for peer in d["results"]:
        print(peer["name"])
