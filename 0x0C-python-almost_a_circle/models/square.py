#!/usr/bin/python3
"""
    This module contain class Square which inherits from the
    class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square implements rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            initialises Square (overrides Rectangle init)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            The getter method of the size instance attribute

            Returns:
                returns the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            The setter method of the size instance method

            Arguments:
                value: the value to set to the width and height attribute
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            The function updates the attributes of the Square instance using
            the args and kwargs variable arguments.
            kwargs is skipped if args is not empty.

            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
        """

        if args and len(args) != 0:
            for arg_i in range(len(args)):
                if arg_i == 0:
                    self.id = args[arg_i]
                elif arg_i == 1:
                    self.size = args[arg_i]
                elif arg_i == 2:
                    self.x = args[arg_i]
                else:
                    self.y = args[arg_i]
        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                else:
                    self.__setattr__(key, val)

    def __str__(self):
        """
            Overloading __str__ function
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def to_dictionary(self):
        """
            This function returns the dictionary representation of a 
            Square instance
        """
        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
