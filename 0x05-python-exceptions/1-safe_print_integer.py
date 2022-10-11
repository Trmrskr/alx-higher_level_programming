#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
    except Exception as error:
        return False
    else:
        return True
