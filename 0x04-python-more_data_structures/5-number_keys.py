#!/usr/bin/python3
def number_keys(a_dictionary):
    """Returns the number of keys in a dictionary.

    Args:
        a_dictionary: A dictionary to count number of keys

    Returns:
        The number of keys in a_dictionary
    """

    keys = 0
    for key, val in a_dictionary.items():
        keys += 1
    return keys
