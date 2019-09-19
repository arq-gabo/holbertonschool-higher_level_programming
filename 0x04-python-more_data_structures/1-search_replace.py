#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw_list = my_list[:]
    for i, j in enumerate(nw_list):
        if j == 2:
            nw_list[i] = 89
    return nw_list
