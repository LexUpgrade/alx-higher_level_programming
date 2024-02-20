#!/usr/bin/python3
"""Defines a function 'read_file'."""


def read_file(filename=""):
    """Reads a text file (UTF-8) and prints it to stdout.

    Args:
        filename = (str): Name of the file to read and print
    """

    with open(filename) as f:
        print(f.read())
