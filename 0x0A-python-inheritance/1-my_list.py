#!/urs/bin/python3
"""Defines a class."""


class MyList(list):
    """A class that inherits from list.

    Args:
        list: A base class.
    """

    def __init__(self):
        """Initializes the object."""
        super().__init__()

    def print_sorted(self):
        """Prints a sorted list."""
        print(sorted(self))
