#!/usr/bin/python3
"""This file contains the add integer function"""

def add_integer(a, b=98):
    """
        Takes in 2 arguments

        Args:
            a (float, int): the first argument
            b (float, int): the second argument

        Return:
            the sum of the 2 integers
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a+b
