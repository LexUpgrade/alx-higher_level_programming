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
        """Returns an attribute"""
        
        return self.__size

    @size.setter
    def size(self, value):
        """Sets attributes."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with the '#' character."""

        if self.__size == 0:
            print()
        else:
            for i in range(int(self.__size)):
                for j in range(int(self.__size)):
                    print("#", end="")
                print()
