#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle.

    Attributes:
        number_of_instances (int): Keeps track of the number of Rectangle instances.
        print_symbol (any): Represents the symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets or sets the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle, raising errors for invalid values.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets or sets the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle, raising errors for invalid values.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the Rectangle, considering special cases."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns the printable representation of the Rectangle using the specified symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        
        rect = [str(self.print_symbol) * self.__width for _ in range(self.__height)]
        return "\n".join(rect)

    def __repr__(self):
        """Returns a string representation of the Rectangle for eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when a Rectangle instance is deleted and updates the instance count."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
