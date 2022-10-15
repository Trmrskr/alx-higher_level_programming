#!/usr/bin/python3
"""Instantiation of the Square class with a private variable
Attributes:
    __init__(function): the constructor function for initializing
        the size variable
    __size (int): the private variable to be initialized
    __position (tuple): private variable to hold position of cursor
"""


class Square:
    """The is the class level of the Square class."""

    def __init__(self, size=0, position=(0, 0)):
        """The constructor level of the Square class
        Args:
            size (int): the size to initialize this.size with
            position (tuple): the position to initialize with
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if (type(position) is not tuple or len(position) != 2 or
            (type(position[0]) is not int or type(position[1]) is not int) or
                (position[0] < 0 or position[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def __str__(self):
        """This function defines an user appealing action of the instance of
        this class when called inside a function
        """
        square_str = ""
        if self.__size > 0:
            for i in range(0, self.__position[1]):
                square_str += "\n"
            for j in range(0, self.__size):
                square_str += ' ' * self.__position[0]
                square_str += '#' * self.__size + '\n'
        else:
            square_str += ""
        return square_str[:-1]

    def __lt__(self, other):
        """The rich comparison operator: less than
        (Python documentation-> Data Models->Special method names)

            Args:
                other: the other square to compare against

            Returns:
                True or false
        """
        return self.size < other.size

    def __le__(self, other):
        """The rich comparison operator: less than or equal to
        (Python documentation-> Data Models->Special method names)

            Args:
                other: the other square to compare against

            Returns:
                True or false
        """
        return self.size <= other.size

    def __eq__(self, other):
        """The rich comparison operator: equal to
        (Python documentation-> Data Models->Special method names)

            Args:
                other: the other square to compare against

            Returns:
                True or false
        """
        return self.size == other.size

    def __ne__(self, other):
        """The rich comparison operator: not equal to
        (Python documentation-> Data Models-> Special method names)

            Args:
                other: the other square to compare against

            Returns:
                True or false
        """
        return self.size != other.size

    def __gt__(self, other):
        """The rich comparison operator: greater than
        (Python documentation-> Data Models-> Special method names)

            Args:
                other: the other square to compare against

            Returns:
                True or false
        """
        return self.size > other.size

    def __ge__(self, other):
        """The rich comparison operator: greater than or equal to
        (Python documentation-> Data Models-> Special method names)

            Args:
                other: the other square to compare against

            Returns:
                True or false
        """
        return self.size >= other.size

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

    @property
    def position(self):
        """This returns the position instance variable"""
        return self.__position

    @position.setter
    def position(self, position):
        """This method sets the position of the position private
        instance variables
        """

        if (type(position) is not tuple or len(position) != 2 or
            (type(position[0]) is not int or type(position[1]) is not int) or
                (position[0] < 0 or position[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """method prints a square with positioning"""
        if self.__size > 0:
            for i in range(0, self.__position[1]):
                print()
            for j in range(0, self.__size):
                print(' ' * self.__position[0], end="")
                print('#' * self.__size)
        else:
            print()
