#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = matrix
    b = matrix
    c = len(a)
    d = len(b)
    nw_matrix = [[a[i][j] * b[i][j] for j in range(c)] for i in range(d)]
    return(nw_matrix)
