#!/usr/bin/python3
"""Algorithm for finding a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers efficiently."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
