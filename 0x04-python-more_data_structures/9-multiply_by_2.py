#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    for keys in a_dictionary.keys():
        a_dictionary[keys] *= 2
    return a_dictionary
