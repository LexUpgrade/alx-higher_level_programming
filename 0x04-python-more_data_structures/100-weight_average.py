#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all integer tuple.

    Args:
        my_list: A list of tuples

    Returns:
        Weighted average of all integers tuple.
    """

    if not my_list:
        return 0
    num = 0
    den = 0
    for tup in my_list:
        num += tup[0] * tup[1]
        den += tup[1]

    return (num / den)
