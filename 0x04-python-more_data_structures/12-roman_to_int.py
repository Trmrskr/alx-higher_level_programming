#!/usr/bin/python3

def get_int_value(xter):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    for r_xter, value in roman_values.items():
        if r_xter == xter:
            return value
    return 0

def roman_to_int(roman_string):
    num_pie = 0
    next_xter_value = 0
    prev_xter_value = 0

    if (roman_string is None or type(roman_string) is not str):
        return 0

    rs_len = len(roman_string)

    for i in range(0, rs_len):
        cur_xter_value = get_int_value(roman_string[i])
        if cur_xter_value == 0:
            return 0

        ni = i+1
        if ni < rs_len:
            next_xter_value = get_int_value(roman_string[ni])
        else:
            next_xter_value = 0
        
        if (cur_xter_value < next_xter_value):
            prev_xter_value = cur_xter_value
        else:
            num_pie += (cur_xter_value - prev_xter_value)
            prev_xter_value = 0
    return (num_pie)
