#!/usr/bin/python3
Square = __import__('101-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

my_square_4 = Square(5, (4, 1))
print(my_square_4)

print("--")

my_square_5 = Square(5, (4, 1))
print(my_square_5)
