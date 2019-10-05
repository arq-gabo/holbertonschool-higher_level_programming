#!/usr/bin/python3

"""
add_integer module
"""


def say_my_name(first_name, last_name=""):
    """Function for concatenate two arguments"""

    if type(first_name) is not str:
        """Varify type value of the argument"""
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        pass

    print("My name is {} {}".format(first_name, last_name))
