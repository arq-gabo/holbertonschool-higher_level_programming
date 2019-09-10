#!/usr/bin/python3
import random
text = "Last digit of"
text2 = "and is less than 6 and not 0"
number = random.randint(-10000, 10000)
lastdigit = number % 10 if number >= 0 else (number * -1) % 10
if lastdigit > 5:
    print("{} {} is {} and is greater than 5".format(text, number, lastdigit))
elif lastdigit == 0:
    print("{} {} is 0 and is 0".format(text, number))
else:
    print("{} {} is {} {}".format(text, number, lastdigit, text2))
