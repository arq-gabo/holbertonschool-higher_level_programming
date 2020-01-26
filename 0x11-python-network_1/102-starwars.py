#!/usr/bin/python3
"""
    STAR WARS API MODULE
"""


import sys
import requests


if __name__ == "__main__":

    url = 'https://swapi.co/api/people/'
    payl = {'search': sys.argv[1]}
    pag = 2

    a = requests.get(url, params=payl)
    try:
        json_data = a.json()
        print("Number of results: {}".format(json_data.get('count')))

        for test in json_data['results']:
            print(test.get('name'))
            for b in test.get('films'):
                respons = requests.get(b)
                data = respons.json()
                print("\t{}".format(data.get('title')))

        while json_data.get('next') is not None:
            payl2 = {'search': sys.argv[1], 'page': page}
            response = requests.get(url, params=payl2)
            json_data = response.json()

            for result in json_data['results']:
                print(result.get('name'))
                for c in result.get('films'):
                    respons = requests.get(c)
                    data = resp.json()
                    print("\t{}".format(data.get('title')))

            pag = pag + 1
    except ValueError:
        print("Not a valid JSON")
