#!/usr/bin/python3
"""Defines a function 'append_write'."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file

    Args:
        filename (str): Name of a file to appends <text> to.
        text (str): Text to append to <filename>.

    Returns:
        Number of characters added to <filename>.
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
