#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    cp_list = my_list[:]
    for i, j in enumerate(my_list):
        if j % 2 == 0:
            cp_list[i] = True
        else:
            cp_list[i] = False
    return cp_list
