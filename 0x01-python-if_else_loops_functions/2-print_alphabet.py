#!/usr/bin/python3
"""Print the alphabets in lowercase, not followed by a new line."""

for char in range(97, 123):
    print("{}".format(chr(char)), end="")
