#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list.

    Args:
        my_list: List for computation

    Returns:
        A list of validation
    """

    validation = [False for i in range(len(my_list))]
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            validation[i] = True

    return validation
