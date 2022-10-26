#!/usr/bin/python3
"""Defines a function that adds an attribute to an object"""


def add_attribute(obj, attr_name, attr_value):
    """This function adds a new attribute to a function
    Argument:
        obj: the object to add attribute to
        attr_name: the name to add to the object
        attr_value: the value to be added to @attr_name
    Raises:
        TyperError: if attribute cannot be added
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
