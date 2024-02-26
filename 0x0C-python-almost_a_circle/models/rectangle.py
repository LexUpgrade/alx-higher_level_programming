#!/usr/bin/python3
"""Defines a <Rectangle> class."""
from models.base import Base


class Rectangle(Base):
    """A class <rectangle> that inherits from <Base>."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates an instance of a <Rectangle>

        Args:
            width (int): The width of the <Rectangle>
            height (int): The height od the <Rectangle>
            x (int): The x coordinate of the new <Rectangle>
            y (int): The y coordinate of the new <Rectangle>
            id (int): The identity of the new <Rectangel>
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get/set a <width> attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/set a <height> attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get/set an <x> attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get/set a <y> attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
