#!/usr/bin/python3
"""This file contains the class_to_json function"""


def class_to_json(obj):
    """function returns the obj dictionary of obj

    Argument:
        obj: the object whose dictionary description is to be returned

    Return:
        the obj.__dict__
    """
    return obj.__dict__
