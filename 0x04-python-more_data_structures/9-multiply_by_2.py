#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic_mult = a_dictionary.copy()
    dic_mult.update((x, y*2) for x, y in dic_mult.items())
    return dic_mult
