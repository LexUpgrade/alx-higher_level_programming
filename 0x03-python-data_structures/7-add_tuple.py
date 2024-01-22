#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns:
        Sum of both tuples
    """

    new_tuple = ()
    num1 = tuple_a + (0, 0)
    num2 = tuple_b + (0, 0)
    new_tuple = ((num1[0] + num2[0]), (num1[1] + num2[1]))
    return new_tuple
