#!/usr/bin/python3
def write_file(filename="", text=""):
    """Function for write in a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return(f.write(text))
