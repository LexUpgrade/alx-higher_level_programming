#!/usr/bin/python3
"""Defines a class that inherits from 'BaseGeometry'."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes an instance of Rectangle.

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Prints and return an info of arguments of the class."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
