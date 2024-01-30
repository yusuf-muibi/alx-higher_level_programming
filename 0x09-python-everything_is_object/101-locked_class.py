#!/usr/bin/python3
"""Defines a locked class."""

class LockedClass:
    """
    Restricts the creation of new attributes in LockedClass,
    allowing only the attribute 'first_name' to be created.
    """

    __slots__ = ["first_name"]
