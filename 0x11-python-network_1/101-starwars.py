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

        while json_data.get('next') is not None:
            payl2 = {'search': sys.argv[1], 'page': pag}
            respon = requests.get(url, params=payl2)
            json_data = respon.json()

            for result in json_data['results']:
                print(result.get('name'))

            pag = pag + 1

    except ValueError:
        print("Not a valid JSON")
