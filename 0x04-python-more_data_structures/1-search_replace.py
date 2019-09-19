#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw_list = my_list[:]
    nw_list[search - 1] = replace
    return nw_list
