#!/usr/bin/python3
"""
add_integer module
"""


def add_integer(a, b=98):
    """Function with two argument"""

    if type(a) is float:
        """casting value to int"""
        a = int(a)
    if type(b) is float:
        """casting value to int"""
        b = int(b)

    if type(a) is not int or type(a) is bool:
        """raise error"""
        raise TypeError("a must be an integer")

    if type(b) is not int or type(b) is bool:
        """raise error"""
        raise TypeError("b must be an integer")

    return a + b
