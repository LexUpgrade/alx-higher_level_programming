#!/usr/bin/python3
"""Defines a function 'load_from_json_file'."""


def load_from_json_file(filename):
    """Creates an object from a 'JSON file'.

    Args:
        filename (str): Filename to load from.
    """
    import json

    with open(filename, 'r') as f:
        return json.load(f)
