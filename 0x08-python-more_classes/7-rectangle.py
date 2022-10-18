#!/usr/bin/python3
""""Rectangle class with attributes"""


class Rectangle:
    """
    Rectangle class: creates a rectangle class

    Attributes:
        number_of_instances (int): a class field which counts the
        number of instance of this class
        width (int): The width of the rectangle
        height (int): the height of the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        """The Rectangle constructor property:
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise TypeError("height must be >= 0")
        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__width*self.__height

    def perimeter(self):
        """Returns the perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width+self.__height)

    def __str__(self):
        """Returns the string representation of the Rectangle"""
        rect_str = ""

        if self.__width <= 0 or self.__height <= 0:
            return rect_str

        for i in range(self.__height):
            rect_str += str(self.print_symbol)*self.__width + "\n"
        return rect_str[:-1]

    def __repr__(self):
        """Returns the official string representation of the Rectangle"""
        rect_repr = ""

        rect_repr += "Rectangle(" + str(self.__width)
        rect_repr += ", " + str(self.__height) + ")"
        return (rect_repr)

    def __del__(self):
        """The rectangle deconstructor function"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
