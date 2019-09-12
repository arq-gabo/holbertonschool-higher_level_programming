#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))

    for x, y in enumerate(sys.argv):
        if x > 0:
            if len(sys.argv) == 2:
                print("{:d}: {:s}".format(x, y))
            elif len(sys.argv) > 2:
                print("{:d}: {:s}".format(x, y))
