#!/usr/bin/python3
""" This module contains a script which loads and offloads from a json file """

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if filename not in os.listdir(os.getcwd()):
    """
        if file is not in list of files and directory in current
        working directory do the following
    """
    my_list = []
else:
    my_list = load_from_json_file("add_item.json")

""" empty or no empty list, add sys.argv to file """
for arg in sys.argv[1:]:
    my_list.append(arg)
save_to_json_file(my_list, "add_item.json")
