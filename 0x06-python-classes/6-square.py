#!/usr/bin/python3
"""Declares a new class."""


class Square:
    """A square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new instance of Square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                all(not isinstance(num, int) for num in value) or
                all(num < 0 for num in value)):
            raise TypeError("position must be a tuple of two positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with the '#' character."""

        if self.__size == 0:
            print()
            return
        
        [print() for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(' ', end='') for i in range(0, self.__position[0])]
            [print('#', end='') for i in range(0, self.__size)]
            print()

