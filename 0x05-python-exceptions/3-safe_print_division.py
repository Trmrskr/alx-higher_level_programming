#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        print("Inside result:", end=" ")
        div = a/b
    except ZeroDivisionError:
        div = None;
    finally:
        print("{}".format(div))
        return div
