#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list.

    Args:
        my_list: A list of integers

    Returns:
        Sum of all unique numbers in my_list.
    """

    sum_up = 0
    new_list = []
    for i in my_list:
        if i not in new_list:
            sum_up += i
            new_list.append(i)
    return sum_up
