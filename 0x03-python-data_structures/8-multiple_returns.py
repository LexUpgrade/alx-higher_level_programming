#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with the length and first character of a string

    Args:
        sentence: String to compute

    Returns:
        0 and None if the string is empty, otherwise the length or
        first character of the string
    """

    if sentence:
        return ((len(sentence), sentence[0]))
    else:
        return (0, None)
