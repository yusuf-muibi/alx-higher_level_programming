#!/usr/bin/python3
"""Algorithm for finding a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers efficiently."""
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]

        elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            right = mid - 1

        else:
            left = mid + 1

    return list_of_integers[left]
