#!/usr/bin/python3
""" This module contains the function load_from_json_file """
import json


def load_from_json_file(filename):
    """ This function loads from json file

        Argument:
            filename: the name of the file to be read from
        Return:
            The object python object read from the file
    """

    with open(filename, encoding="utf") as json_file:
        my_obj = json.load(json_file)
        return my_obj
