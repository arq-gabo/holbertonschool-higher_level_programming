#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    my_list2 = [a[0] * a[1] for a in my_list]
    my_list3 = [b[1] for b in my_list]
    return sum(my_list2) / sum(my_list3)
