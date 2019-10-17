#!/usr/bin/python3

"""Module"""


import json


def load_from_json_file(filename):
    """"""
    new_str = ""
    with open(filename, "r", encoding='utf-8') as f:
        for i in f:
            new_str += i
    return json.loads(new_str)
