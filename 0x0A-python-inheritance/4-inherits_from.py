#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj: The object to check.
        a_class: The specified class to check against.
    Returns:
        True if obj is instance of a class inherited from a_class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
