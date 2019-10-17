#!/usr/bin/python3

"""Sava tu json module"""


import json


def save_to_json_file(my_obj, filename):
    """Method for safe Json file"""
    with open(filename, "w", encoding="utf-8") as f:
        return(f.write(json.dumps(my_obj)))
