#!/usr/bin/python3
for rev in reversed(range(97, 123)):
    if rev % 2 != 0:
        rev = rev - 32
    print("{}".format(chr(rev)), end='')
