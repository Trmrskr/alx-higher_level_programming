#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    maxim = list(a_dictionary.values())[0]
    for k, v in a_dictionary.items():
        if v > maxim:
            maxim = v
            key = k
    return key
