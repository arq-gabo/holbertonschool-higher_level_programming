#!/usr/bin/python3
def multiple_returns(sentence):
    lgth = len(sentence)
    if lgth > 0:
        first_char = sentence[0]
    else:
        None
    tup = lgth, first_char
    return(tup)
