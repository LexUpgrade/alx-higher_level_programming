#!/usr/bin/python3
"""Defines a function 'is_kind_of_class'"""


def is_kind_of_class(obj, a_class):
    """Checks if the object 'obj' is an instance a_class

    Args:
        obj (any): A class to check
        a_class (type): Class to match 'obj' with

    Return:
        True - if 'obj' is an instance of 'a_class'
        False - otherwise
    """

    if isinstance(obj, a_class):
        return True
    return False
