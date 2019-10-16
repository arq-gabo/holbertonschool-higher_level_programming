#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """Function for print N number of lines in a txt file"""
    with open(filename, "r", encoding="utf-8") as f:
        for i, lines in enumerate(f):
            if i < nb_lines or nb_lines <= 0:
                print(lines, end='')
            else:
                break
