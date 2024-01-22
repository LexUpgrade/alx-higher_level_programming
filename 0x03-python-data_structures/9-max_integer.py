#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds and return the biggest integer in a list

    Args:
        my_list: List to sought for biggest value in it range

    Returns:
        Maximum value in a list
    """

    if len(my_list) == 0:
        return None
    else:
        sorted_list = my_list
        sorted_list.sort()
        return sorted_list[len(sorted_list) - 1]
