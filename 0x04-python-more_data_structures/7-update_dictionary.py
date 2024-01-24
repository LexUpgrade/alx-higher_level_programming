#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: A dictionary to manipulate
        key: A key to add or modify
        value: A value to add

    Returns:
        Modified version of a_dictionary
    """

    a_dictionary[key] = value
    return a_dictionary
