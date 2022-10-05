#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, dic_val in a_dictionary.items():
        if dic_val == value:
            del a_dictionary[key]
    return a_dictionary
