#!/usr/bin/python3


"""Module Base"""

import json


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init Method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method for standar format of JSON"""
        base_list = []
        if list_dictionaries is None or len(list_dictionaries) is 0:
            list_dictionaries = []
            return list_dictionaries
        if type(list_dictionaries) is not list:
            base_list.append(list_dictionaries)
        else:
            base_list = list_dictionaries

        return json.dumps(base_list)
