#!/usr/bin/python3
"""This module contains an empty class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry just simply pass when instantiated

    Attribute:
        area: a public method
    """
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
