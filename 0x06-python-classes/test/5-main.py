#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(30)
my_square.my_print()

print("--")

my_square.size = 100
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

my_square.size = 125
my_square.my_print()

print("--")
