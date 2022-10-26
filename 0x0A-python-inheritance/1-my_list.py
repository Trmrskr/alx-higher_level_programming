#!/usr/bin/python3
"""This module contains MyList class which inherits from list class"""


class MyList(list):
    """ MyList class: inherits from list class

        Attributes:
            print_sorted: a function which prints this class in sorted order
    """
    def __init__(self):
        """ The constructor method of the MyList class """
        super().__init__()

    def print_sorted():
        """ A function that prints self in sorted order """
        print(sorted(self))
