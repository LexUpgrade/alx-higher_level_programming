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
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
