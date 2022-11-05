#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(1, 2)
    r1.display()

    print("No x and y---")

    r2 = Rectangle(1, 2, 1)
    r2.display()

    print("No y---")

    r3 = Rectangle(4, 6, 2, 1)
    r3.display()

    print("No x---")

    r4 = Rectangle(3, 2, 1, 0)
    r4.display()

    print("Both x and y---")
