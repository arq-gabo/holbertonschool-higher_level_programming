#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dic = []
    for a in a_dictionary:
        if a_dictionary[a] is value:
            new_dic.append(a)
    for b in new_dic:
        del a_dictionary[b]
    return(a_dictionary)
