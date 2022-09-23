#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    args = args[1:]
    i = 1
    if len(args) == 1:
        print("1 argument:")
        print("1: {}".format(args[0]))
    elif len(args) == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(args)))
        for each in args:
            print("{}: {}".format(i, each))
            i += 1
