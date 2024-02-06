#!/usr/bin/python3
"""Declares a new class."""


class Square:
    """A square class."""

    def __init__(self, size=0):
        """Initialize a new instance of Square.

        Args:
            size (int): The size of the new square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square."""

        return self.__size**2
