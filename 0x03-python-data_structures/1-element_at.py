#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrives an element from a list

    Args:
        my_list: A list to retrive from
        idx: Index to fetch

    Returns:
        None if idx is negative or out of bound, otherwise
        value at index idx
    """

    count = len(my_list)
    if idx < 0 or idx > count:
        return None
    else:
        return (my_list[idx])
