#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific index

    Args:
        my_list: List to modify
        idx: Index to overwrite
        element: Element for replacement

    Return:
        None if idx is negative or out of bound, otherwise
        newly modified list
    """

    count = len(my_list) - 1
    if idx < 0 or idx > count:
        return (my_list)
    else:
        my_list[idx] = element
 
    return (my_list)
