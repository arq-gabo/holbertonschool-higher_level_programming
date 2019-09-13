#!/usr/bin/python3
import sys
if __name__ == "__main__":
    number = 0
    for x in sys.argv[1:]:
        number += int(x)
    print(number)
