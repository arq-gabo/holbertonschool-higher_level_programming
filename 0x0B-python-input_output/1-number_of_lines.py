#!/usr/bin/python3
def number_of_lines(filename=""):
    """Function for count number lines"""
    with open(filename, "r", encoding="utf-8") as f:
        i = 0
        for j in f:
            i += 1
        return i
