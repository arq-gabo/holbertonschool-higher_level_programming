#!/usr/bin/python

"""Module of the 11-student"""


class Student:
    """Create class student"""

    def __init__(self, first_name, last_name, age):
        """Init method initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method to json"""
        return self.__dict__
