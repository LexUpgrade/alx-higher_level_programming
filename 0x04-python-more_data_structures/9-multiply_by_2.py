#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary: A simple dictionary

    Returns:
        A new dictionary with all values multiplies of a_dictionary
    """

    new_dic = {}
    for k, v in a_dictionary.items():
        new_dic[k] = v * 2

    return new_dic
