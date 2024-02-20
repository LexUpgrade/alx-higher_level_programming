#!/usr/bin/python3
"""Defines a function 'save_to_json_file'."""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation.
    Args:
        my_obj (str): An object to write to <filename>.
        filename: File to write <my_obj> to.
    """
    import json

    with open(filename, 'w') as j_file:
        json.dump(my_obj, j_file)
