#!/usr/bin/python3
"""Defines a function 'from_json_string'."""


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by
        a JSON string.
    """
    import json

    return json.loads(my_str)
