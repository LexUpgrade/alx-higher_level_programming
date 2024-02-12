#!/usr/bin/python3
"""Defines a class"""


class Rectangle:
    """A class Rectangle"""

    def __init__(self, width=0, height=0):
        """Creates an instance of class Rectangle

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle

        """

        self.width = width
        self.height = height

        @property
        def width(self):
            """Get/set attribute width."""
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """Get/set attribute height."""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integre")
            elif value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
