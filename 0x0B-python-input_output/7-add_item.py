#!/usr/bin/python3

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if filename not in os.listdir(os.getcwd()):
    my_list = []
    save_to_json_file(my_list, "add_item.json")
else:
    my_list = load_from_json_file("add_item.json")
    for arg in sys.argv[1:]:
        my_list.append(arg)
    save_to_json_file(my_list, "add_item.json")
