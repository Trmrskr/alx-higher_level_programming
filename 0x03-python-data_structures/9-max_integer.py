#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return "None"
    maxim = my_list[0]
    for xger in my_list:
        if xger > maxim:
            maxim = xger
    return maxim
