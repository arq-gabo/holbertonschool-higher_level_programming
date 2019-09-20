#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_key = max(a_dictionary, key=lambda k: a_dictionary[k])
    else:
        return None
    return max_key
