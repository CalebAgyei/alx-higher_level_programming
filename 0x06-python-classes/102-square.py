#!/usr/bin/python3

"""Defines a class square"""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initalizing square.

        Args:
            size: The size of the square
        """
        self.size = size

    @property
    def size(self):
        """Access private instance attribute 'size'."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set or update private instance attribute 'size'.

        Args:
            value: New value to update 'size'
        """
        try:
            if not isinstance(value, int) or not isinstance(value, float):
                raise TypeError("size must be a number")
            elif value < 0:
                raise ValueError("size must be >= 0")
        except Exception:
            print("")
        self.__size = value

    def area(self):
        """Calculate the current square area

        Returns:
            Current square area
        """
        return (self.__size * self.__size)

    def __call__(self):
        return (self.__size * self.__size)
