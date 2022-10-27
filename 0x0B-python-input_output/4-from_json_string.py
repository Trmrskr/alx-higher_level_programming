#!/usr/bin/python3
""" A function that converts Json string to object"""
import json

def from_json_string(my_str):
    """ function from_json_string
        Argument:
            my_str (json string): the string to be parsed to python object
        Return:
            a python object
    """

    return json.loads(my_str)
