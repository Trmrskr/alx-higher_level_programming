#!/usr/bin/python3

def no_c(my_string):
    my_str_list = list(my_string)
    i = 0
    for xter in my_str_list:
        xter_ord = ord(xter)
        if xter_ord == 99 or xter_ord == 67:
            my_str_list.pop(i)
        i = i + 1
    return ' '.join(str(x) for x in my_str_list)
