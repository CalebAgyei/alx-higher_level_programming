#!/usr/bin/python3

"""Defines a class square"""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initalizing square.

        Args:
            size: The size of the square
        """
        self.__size = size
        try:
            if type(self.__size) != 'int':
                raise TypeError
            elif self.__size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
