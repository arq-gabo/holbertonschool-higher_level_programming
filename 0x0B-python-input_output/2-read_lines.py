#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, "r", encoding="utf-8") as f:
        for i, lines in enumerate(f):
            if i < nb_lines or nb_lines <= 0:
                print(lines, end='')
            else:
                break
