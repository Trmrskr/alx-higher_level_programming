#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) <= 0:
        return 0
    sum = 0
    for num in set(my_list):
        sum += num
    return sum
