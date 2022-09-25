#!/usr/bin/python3

def remove_char_at(str, n):
    strlen = len(str)
    
    if strlen >= 0 or n <= strlen:
        for i in range(0, strlen):
            if i >= n:
                str[i] = str[i + 1]

    print("{}".format(str))

