#!/usr/bin/python3
for x in range(100):
    if x >= 0 and x <= 98:
        print("{:0>2}, ".format(x), end='')
    else:
        print("99")
