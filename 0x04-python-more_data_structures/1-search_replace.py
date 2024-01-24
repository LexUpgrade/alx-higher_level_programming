#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurances of an element by another in a new list.

    Args:
        my_list: List consisting default values
        search: Element to replace in the list
        replace: New element for replacement

    Returns:
        A new editied list.
    """

    new_list = [0 * len(my_list) for i in range(len(my_list))]
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list[i] = replace
        else:
            new_list[i] = my_list[i]

    return new_list
