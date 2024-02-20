#!/usr/bin/python3
"""Defines a function 'write_file'."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8)

    Args:
        filename (str): Name of the file to write to.
        text (str): Text to write into 'filename'.

    Returns:
        The number of characters written.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
