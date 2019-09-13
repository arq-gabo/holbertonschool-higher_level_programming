#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from calculator_1 import *
    if len(sys.argv) == 4:
        a = sys.argv[1]
        b = sys.argv[3]
        op = sys.argv[2]
        if op == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
            exit(0)
        elif op  == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
            exit(0)
        elif op  == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
            exit(0)
        elif op  == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
