#!/usr/bin/python3

def uppercase(str):
    for xter in str:
        xter_ord = ord(xter)
        if xter_ord >= 97 and xter_ord <= 122:
            print("{:c}".format(xter_ord-32), end='')
        else:
            print("{:c}".format(xter_ord), end='')
    print("")
