#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj: The object to check.
        a_class: The specified class to compare against.
    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
