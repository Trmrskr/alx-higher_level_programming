#!/usr/bin/python3
"""
This module contains the append after function
"""

def append_after(file_name, search_text, text_append):
    """The append namspace"""

    new_data = ""
    with open(file_name, "r", encoding="utf-8") as fil:
        for line in fil:
            new_data += line
            if search_text in line:
                new_data += text_append

    with open(file_name, "w", encoding="utf-8") as fil:
        n = fil.write(new_data)
        print(n)
