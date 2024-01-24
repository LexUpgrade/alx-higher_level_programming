#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary.

    Args:
        a_dictionary: A simple dictionary
        key: key to delete

    Returns:
        Modified version of a_dictionary
    """

    if a_dictionary.get(key, 0) != 0:
        del a_dictionary[key]
    return a_dictionary
