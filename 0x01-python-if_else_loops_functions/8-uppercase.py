#!/usr/bin/python3

def uppercase(str):
    for xter in str:
        xter_ord = ord(xter)
        lowercase = xter_ord >= 97 and xter_ord <= 122
        print("{:c}".format(xter_ord-32 if lowercase else xter_ord), end='')
    print("")
