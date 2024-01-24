#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys.

    Args:
        a_dictionary: A dictionary to print in an ordered list

    Returns:
        None
    """

    new_list = list(a_dictionary)
    new_list.sort()

    for i in new_list:
        print("{}: {}".format(i, a_dictionary.get(i)))
