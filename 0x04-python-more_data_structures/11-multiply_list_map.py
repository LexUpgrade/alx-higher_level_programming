#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Returns a list with all values multiplied by a number
        without using any loop.

    Args:
        my_list: A list of integers
        number: Number to multiply integers by

    Returns:
        A new list consisting of the multiplied values
    """

    new_list = list(map(lambda x: x * number, my_list))
    return new_list
