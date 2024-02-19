#!/usr/bin/python3
"""Defines a class 'BaseGeometry'."""


class BaseGeometry:
    """A BaseGeometry class."""
    
    def area(self):
        """An area method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates arguments."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
