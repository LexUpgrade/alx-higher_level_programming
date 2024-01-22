#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position
        without modifying the original list

    Args:
        my_list: Original list
        idx: Index to modify
        element: Element for replacement

    Returns:
        None if idx is negative or out of bound, otherwise
        newly modified list
    """

    count = len(my_list) - 1
    if idx < 0 or idx > count:
        return my_list
    else:
        new_list = [0 for i in range(len(my_list))]
        for i in range(len(my_list)):
            if i == idx:
                new_list[idx] = element
            else:
                new_list[i] = my_list[i]
        return (new_list)
