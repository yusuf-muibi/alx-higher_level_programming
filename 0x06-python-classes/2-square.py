#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Represent a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__: Initializes a new Square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        # Check if size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # Check if size is less than 0
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
