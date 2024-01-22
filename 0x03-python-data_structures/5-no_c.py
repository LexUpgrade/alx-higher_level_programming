#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters c and C from a string

    Args:
        my_string: String to modify

    Returns:
        Newly modify string
    """

    new_string = my_string.translate({ord(i): None for i in 'Cc'})
    return (my_string)
