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

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
