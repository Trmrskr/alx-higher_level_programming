#!/usr/bin/python3

for tenth_digit in range(10):
    for unit_digit in range(10):
        if unit_digit > tenth_digit:
            if tenth_digit == 8 and unit_digit == 9:
                print("{:d}{:d}".format(tenth_digit, unit_digit))
            else:
                print("{:d}{:d}".format(tenth_digit, unit_digit), end=", ")
