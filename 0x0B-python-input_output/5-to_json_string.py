#!/usr/bin/python3

"""module for convert object to json"""

import json


def to_json_string(my_obj):
    """Function for convert a python object to json"""
    return(json.dumps(my_obj))
