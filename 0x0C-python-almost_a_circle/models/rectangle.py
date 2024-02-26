#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    """A class <rectangle that inherits from <Base>."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates an instance of a <Rectangle>

        Args:
            width (int): The width of the <Rectangle>
            height (int): The height od the <Rectangle>
            x (int): The x coordinate of the new <Rectangle>
            y (int): The y coordinate of the new <Rectangle>
            id (int): The identity of the new <Rectangel>
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
        self.__width = value

    @property
    def height(self):
        """Get/set a <height> attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Get/set an <x> attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Get/set a <y> attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
