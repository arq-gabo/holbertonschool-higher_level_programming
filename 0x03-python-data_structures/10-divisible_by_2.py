def divisible_by_2(my_list=[]):
    cp_my_list = my_list[:]
    for i, j in enumerate(my_list):
        if j % 2 == 0:
            cp_my_list[i] = True
        else:
            cp_my_list[i] = False
    return cp_my_list
