#!/usr/bin/python3
"""This module contains an class Square that inherits from Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Square constructor/instantiation method

        Args:
            size (int): the width/height of the instance of square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """This method calculates the area of the square"""
        return self.__size ** 2
