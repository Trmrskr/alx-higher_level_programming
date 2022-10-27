#!/usr/bin/python3
"""A function that writes to a file"""


def write_file(filename="", text=""):
    """
        The function write_file function

        Argument:
            filename: the name of the file
            text: the string to be written to the file
    """

    with open(filename, "w", encoding="utf-8") as text_file:
        no_char = text_file.write(text)
    return no_char
