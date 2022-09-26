#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return None
    maxim = my_list[0]
    for xger in my_list:
        if xger > maxim:
            maxim = xger
    return maxim
