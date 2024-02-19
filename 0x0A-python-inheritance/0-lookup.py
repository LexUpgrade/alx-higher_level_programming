#!/usr/bin/python3
"""Defines a function"""


def lookup(obj):
    """Returns a list of all available attributes and methods of an object

    Args:
        obj (any type): An object to compute

    Returns:
        A list of all available attributes and methods of an object.
    """

    return list(dir(obj))
