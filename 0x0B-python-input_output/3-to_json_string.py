#!/usr/bin/python3
""" This file contains the function to_json_string"""
import json


def to_json_string(my_obj):
    """
        to_json_string

        Argument:
            my_obj: the object to be jsonify

        Return:
            the json string of the my_obj string
    """

    return json.dumps(my_obj)
