#!/usr/bin/python3
def number_of_lines(filename=""):
    """Function for count number lines"""
    with open(filename, "r", encoding="utf-8") as f:
        for i, j in enumerate(f):
            pass
    return i + 1
