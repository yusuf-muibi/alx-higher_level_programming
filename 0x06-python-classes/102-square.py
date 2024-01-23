#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Define the equality comparison for a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the inequality comparison for a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the less than comparison for a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the less than or equal comparison for a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the greater than comparison for a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the greater than or equal comparison for a Square."""
        return self.area() >= other.area()
