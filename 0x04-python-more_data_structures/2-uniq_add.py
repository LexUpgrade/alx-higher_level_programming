#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list.

    Args:
        my_list: A list of integers

    Returns:
        Sum of all unique numbers in my_list.
    """
    from functools import reduce

    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    sum_up = reduce(lambda x, y: x + y, new_list)
    return sum_up
