#!/usr/bin/python3

"""
Divide a matrix module
"""


def matrix_divided(matrix, div):
    """function for make div operator in a matrix with de div value"""

    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            if type(matrix[a][b]) is int or type(matrix[a][b]) is float:
                pass
            else:
                raise TypeError(err_msg)

    if len(matrix[0]) is not len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    else:
        pass

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    else:
        pass

    try:
        new_matrix = [[round(a / div, 2) for a in lines]for lines in matrix]
    except ZeroDivisionError:
        raise ZeroDivisionError("division by zero")

    return new_matrix
