#!/usr/bin/python3
"""Defines a class 'BaseGeometry'."""


class BaseGeometry:
    """A BaseGeometry class."""

    def area(self):
        """An area method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates arguments.

        Args:
            name (str): The name of the parameter
            value (int): The parameter to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: if value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
