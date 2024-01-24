#!/usr/bin/python3
from functools import reduce
def uniq_add(my_list=[]):
    """Adds all unique integers in a list.

    Args:
        my_list: A list of integers

    Returns:
        Sum of all unique numbers in my_list.
    """

    sum_up = reduce(lambda x, y: x + y, set(my_list))
    return sum_up
