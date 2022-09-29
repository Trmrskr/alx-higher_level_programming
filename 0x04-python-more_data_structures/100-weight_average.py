#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    suma = 0
    numerator = 0
    denominator = 0
    for tuples in my_list:
        suma = tuples[0]*tuples[1]
        numerator += suma
        denominator += tuples[1]
    return numerator/denominator
