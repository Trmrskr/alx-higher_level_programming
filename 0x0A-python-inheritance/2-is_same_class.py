#!/usr/bin/python3
"""This module contains the is_same_class function"""


def is_same_class(obj, a_class):
    """The function checks if obj is an exact instance of a_class

    Argument:
        obj: the object to be checked
        a_class: the class to be compared

    Return: True if obj is an instance of class otherwise false
    """
    if type(obj) is a_class:
        return True
    else:
        return False
