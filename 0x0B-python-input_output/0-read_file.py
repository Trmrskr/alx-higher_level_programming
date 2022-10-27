#!/usr/bin/python3
"""The file contains the read_file function"""


def read_file(filename=""):
    """ The read file function opens and reads a file and prints its
        contents to standard output

        Argument:
            filename: name of file, default to empty
    """
    with open(filename, encoding="utf-8") as text_file:
        print(text_file.read(), end="")
