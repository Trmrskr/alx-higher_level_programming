#!/usr/bin/python3
"""Instantiation of the Square class with a private variable
Attributes:
    __init__(function): the constructor function for initializing
        the size variable
    __size (int): the private variable to be initialized
"""


class Square:
    """The is the class level of the Square class."""

    def __init__(self, size=0):
        """The constructor level of the Square class
        Args:
            size (int): the size to initialize this.size with
        """

        self.__size = size
