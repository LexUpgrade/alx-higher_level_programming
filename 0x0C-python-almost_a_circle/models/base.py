#!/usr/bin/python3
"""Defines a class <Base>."""


class Base:
    """Base Model

    This Represents the "base" for all other classes in project

    Private Class attribute:
        __nd_objects (int): Number of instantiated Bases.
    """

    __nd_objects = 0

    def __init__(self, id=None):
        """Instantiates an instance of a class <Base>

        Args:
            id (int): Identity of new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nd_objects += 1
            self.id = Base.__nd_objects
