#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    no_set = set(set_1) ^ set(set_2)
    return no_set
