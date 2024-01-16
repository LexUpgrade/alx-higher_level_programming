#!/usr/bin/python3
"""Prints the ASCII alpabet, in lowercase except 'q' and 'e',
not followed by a new line."""

for char in range(97, 123):
    if chr(char) != 'q' and chr(char) != 'e':
        print("{}".format(chr(char)), end="")
