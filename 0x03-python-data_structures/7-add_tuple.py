#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    for a in range(len(tuple_a), 2):
        list_a.append(0)
    for b in range(len(tuple_b), 2):
        list_b.append(0)
    new_list = (list_a[0] + list_b[0], list_a[1] + list_b[1])
    return(tuple(new_list))
