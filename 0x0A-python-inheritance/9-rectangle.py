#!/usr/bin/python3
"""This module contains an class BaseGeometry and another Rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Rectangle constructor/instantiation method

        Args:
            width (int): the width of the new rectangle.
            height (int): the height of the the new rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """This method calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the Rectangle class"""
        return "[{}] {:d}/{:d}".format(
                self.__class__.__name__, self.__width, self.__height
                )
