#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % 10 if number >= 0 else (((number * -1) % 10) * - 1)
if lastdigit > 5:
    print("Last digit of", end = ' ')
    print("{} is {} and is greater than 5".format(number, lastdigit))
elif lastdigit == 0:
    print("Last digit of {} is 0 and is 0".format(number))
else:
    print("Last digit of", end = ' ')
    print("{} is {} and is less than 6 and not 0".format(number, lastdigit))
