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
            return []
        if type(list_dictionaries) is not list:
            base_list.append(list_dictionaries)
        else:
            base_list = list_dictionaries

        return json.dumps(base_list)

    @classmethod
    def save_to_file(cls, list_objs):
        """Upload class Base with write a json string"""
        new_list = []
        if list_objs is None:
            return new_list
        else:
            for i in list_objs:
                new_list.append(i.to_dictionary())

        with open("{}.json".format(cls.__name__), "w", encoding='utf-8') as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """Which returns the list of the JSON string representation"""
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)
