#!/usr/bin/python3
""" This file contains the save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """ save_to_json_file is a function that saves a python object
        to a json file

        Args:
            my_obj: object
            filename: textfile name
        """

    with open(filename, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(my_obj))
