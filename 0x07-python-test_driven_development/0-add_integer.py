#!/usr/bin/python3
"""Defines a function for adding integers."""

def add_integer(a, b=98):
    """Returns the sum of integers a and b.

    Float arguments are converted to integers before performing the addition.

    Raises:
        TypeError: If either a or b is neither an integer nor a float.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or float")

    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer or float")


    a = int(a)
    b = int(b)

    return a + b
