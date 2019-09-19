#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw_list = my_list[:]
    for i, j in enumerate(nw_list):
        if j == int(search):
            nw_list[i] = int(replace)
    return nw_list
