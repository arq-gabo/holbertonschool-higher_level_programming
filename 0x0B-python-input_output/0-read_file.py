#!/usr/bin/python3
def read_file(filename=""):
    """function por read the file .txt"""
    with open(filename, "r", encoding="utf-8") as read_file:
        print(read_file.read())
