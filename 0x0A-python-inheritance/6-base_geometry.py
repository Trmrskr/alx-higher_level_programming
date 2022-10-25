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

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (str): The parameter to validate.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is <= 0.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
