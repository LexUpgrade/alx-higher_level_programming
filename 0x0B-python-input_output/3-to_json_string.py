#!/usr/bin/python3
"""Defines a function 'to_json_string'."""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj (any): Object to convert

    Returns:
        JSON representation of <my_obj>.
    """

    import json

    return json.dumps(my_obj)
