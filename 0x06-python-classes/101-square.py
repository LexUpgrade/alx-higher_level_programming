#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Inializes a new square

        Args:
            size (int): Size of the square
            position (tupel(int, int)): Tuple of two integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    @property
    def position(self):
        """Get/set position"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or 
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("posistion must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Gets the area of a square."""
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the character '#'"""
        if self.__size == 0:
            print()
        else:
            [print() for i in range(0, position[1])]
            for i in range(0, len(self.__size)):
                [print(' ', end='') for j in range(0, self.__position[0])]
                [print('#', end='') for k in range(0, self.__size)]
                print()

    def __str__(self):
        """Define the print() representation of a square"""
        if self.__size != 0:
            [print() for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(' ', end='') for j in range(0, self.__position[0])]
                [print('#', end='') for k in range(0, self.__size)]
                if i != self.__size - 1:
                    print("")
            return ("")
