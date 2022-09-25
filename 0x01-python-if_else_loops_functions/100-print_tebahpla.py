#!/usr/bin/python3

xter = 122
while (xter >= 97):
    print("{:c}".format(xter-32 if xter % 2 != 0 else xter), end="")
    xter -= 1
