#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for y in matrix:
        z = 0
        for x in y:
            r_space = len(y)
            z += 1
            if z != r_space:
                print(x, end=' ')
            else:
                print(x, end='')
        print()
