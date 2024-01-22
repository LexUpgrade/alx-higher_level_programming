#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints a list in reverse order

    Args:
        my_list: List to print in reverse

    Returns:
        None
    """
    count = len(my_list) - 1
    for i in range(count, -1, -1):
        print(my_list[i])
