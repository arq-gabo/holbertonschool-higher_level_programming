#!/usr/bin/python3
for x in range(90):
    if x < 89 and x % 10 != 0 and x % 10 >= x / 10:
        print("{:0>2}, ".format(x), end='')
print("89")
