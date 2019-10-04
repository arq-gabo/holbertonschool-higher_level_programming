#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    if type(a) is not int or type(a) is bool:
        raise TypeError("a must be an integer")

    if type(b) is not int or type(b) is bool:
        raise TypeError("b must be an integer")

    return a + b

#print(add_integer(1, 2, 3))
#print(add_integer(50, -2))
#print(add_integer(-4, -7))
#print(add_integer(2.672, 7.564))
#print(add_integer(999999999, 1))
#print(add_integer(3, True))
#print(add_integer(6, [1, 2, 3, 4, 5]))
#print(add_integer(0))
#print(add_integer(1, 2, 3))
