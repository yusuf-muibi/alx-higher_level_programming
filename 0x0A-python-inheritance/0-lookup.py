#!/usr/bin/python3
"""Defines a lookup function for object attribute."""


def lookup(obj):
    """Return a list of the availabe attributes of an object."""
    return (dir(obj))
