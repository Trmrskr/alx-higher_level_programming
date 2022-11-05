#!/usr/bin/python3
"""
    This module contains the class Rectangle which inherits from the Base class.
"""
from models.base import Base


class Rectangle(Base):
    """
        The Rectangle class which inherits from Base.

        Attributes:
            __width (int): holds the width of the rectangle
            __height (int): holds the height of the rectangle
            __x (int): holds the x coordinate of the rectangle
            __y (int): holds the y coordinate of the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initializes the instance of the class..
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            The getter function of the __width
            Returns: __width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            The setter function instance of Rectangele width.
            Args:
                value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
            getter function for instance of Rectangle height
            Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter function for instance Rectangle height
            Args:
                value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
            getter function for x coordinate of Rectangle instance.
            Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            setter function for x coordinate of Rectangle instance.
            Args:
                value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
            getter function for y coordinate of Rectangle instance.
            Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            setter function for y coordinate of Rectangle instance
            Args:
                value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
            Calculates and returns the area of the Rectangle instance.
        """
        return (self.__width * self.__height)

    def display(self):
        """
            Prints the rectangle instance using the # symbol
        """
        print_symbol = "#"

        for off in range(self.__y):
            print()
        for points in range(self.__height):
            print(" " * self.__x, end=" ")
            print(print_symbol * self.__width)

    def __str__(self):
        """
            returns a informal string representation of the rectangle instance
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
            This function updates the Rectangle class by assigning an argument
            to each attribute.
            Args:
                *args -  variable number of non-keyworded args
                **kwargs - variable number of keyworded args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
            returns the dictionary of a rectangle instance
        """
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}
