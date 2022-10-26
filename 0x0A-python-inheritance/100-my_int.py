#!/usr/bin/python3
"""This module contains a class MyInt which inherits from int class"""


class MyInt(int):
    """The MyInt class
    
    Attribute:
        __eq__: equal special method
        __ne__: not equal to special method
    """

    def __eq__(self, other):
        """
            The rich comparison operator __eq__
            Instead returns if not equals

            Attribute:
                other: the other object to be compared against
        """
        return self.real != other

    def __ne__(self, other):
        """
            The rich comparison operator __ne__
            Instead returns equals
            Attribute:
                other: the object to be compared against
        """

        return self.real == other
