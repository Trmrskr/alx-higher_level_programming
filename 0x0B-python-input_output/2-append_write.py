#!/usr/bin/python3
"""This module contains the ``append_write`` file"""


def append_write(filename="", text=""):
    """
        append_write: appends string to a file
        
        Argument:
            filename: the name of the file to be appended to
            text: the string to be appended to the file
    """
    with open(filename, "a", encoding="utf-8") as text_file:
        n_char = text_file.write(text)
    return n_char
