#!/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list.

    Args:
        my_list: A list of integers
        x: The number of elements of my_list to print

    Returns:
        Number of elements printed
    """

    size = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            size += 1
        except IndexError:
            break
    print("")

    return (size)
