#!/usr/bin/python3
"""Defines a function that returns the list of available attributes and methods of a string"""


def lookup(obj):
    return list(dir(obj))
