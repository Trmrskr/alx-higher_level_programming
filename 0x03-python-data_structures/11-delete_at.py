#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if my_list is None:
        return None
    list_len = len(my_list)
    if idx < 0 or idx >= list_len:
        return my_list
    for i in range(0, list_len):
        if i > idx:
            my_list[i-1] = my_list[i]
    del my_list[i]
    return my_list
