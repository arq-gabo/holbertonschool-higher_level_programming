#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            new_matrix[x][y] += matrix[x][y]*matrix[x][y]
    return(new_matrix)
