#!/usr/bin/python3

"""Defines a class square"""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initalizing square.

        Args:
            size: The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the current square area

        Returns:
            Current square area
        """
        return (self.__size * self.__size)
