#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value.

    Args:
        a_dictionary: A simple dictionary

    Returns:
        Key with the highest value

    """

    if a_dictionary:
        value = 0
        for k, v in a_dictionary.items():
            if v >= value:
                value = v
                winner = k
        return winner
