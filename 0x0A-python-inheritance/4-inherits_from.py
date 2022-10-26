#!/usr/bin/python3
"""This module contains inherits_from function"""


def inherits_from(obj, a_class):
    """The function checks if obj inherits_from a_class

    Argument:
        obj: the object to be checked
        a_class: the class to be compared

    Return: True if obj is an instance of class otherwise false
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
