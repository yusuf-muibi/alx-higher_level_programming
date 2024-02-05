#!/usr/bin/python3
"""Defines a function that returns the list of an object"""
def lookup(obj):
    """Returns a list containing the available attributes of an object."""
    return (dir(obj))
