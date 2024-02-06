#!/usr/bin/python3
"""Declares a new class."""


class Square:
    """A square class."""

    def __init__(self, size=0):
        """Initialize a new instance of Square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""

        return self.__size**2
