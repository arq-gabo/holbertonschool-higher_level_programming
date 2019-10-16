#!/usr/bin/python3
def number_of_lines(filename=""):
    """Function for count number lines"""
    with open(filename) as f:
        for i, j in enumerate(f):
            pass
    return i + 1
