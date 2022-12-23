#!/usr/bin/python3
# 1-square.py
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Property of size for the square"""
        return (self.__size)
   
    @size.setter
    def size(self, value):
        """Setting the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square defined"""
        return (self.__size ** 2)
