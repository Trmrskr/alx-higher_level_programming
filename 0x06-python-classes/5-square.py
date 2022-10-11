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
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area: the method calculates the area of the square

            Returns:
                the area given the size
        """
        return self.__size ** 2

    @property
    def size(self):
        """This method returns the size private instance variable
"""

        return self.__size

    @size.setter
    def size(self, size):
        """This method sets the size of the private instance variable"""
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """method prints a square"""
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()


