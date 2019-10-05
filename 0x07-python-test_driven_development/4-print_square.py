#!/usr/bin/python3

"""
print square module
"""


def print_square(size):
    """function for print square"""

    if type(size) is not int:
        """Conditional for check if value is not integer"""
        raise TypeError("size must be an integer")
    elif size < 0:
        """Check is the value is less to zero"""
        raise ValueError("size must be >= 0")
    else:
        pass

    for a in range(size):
        print("#" * size)
