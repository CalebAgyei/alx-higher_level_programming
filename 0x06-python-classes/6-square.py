#!/usr/bin/python3

"""Defines a class square"""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initalizing square.

        Args:
            size: The size of the square
            position: The position of the square
        """
        self.size = size
        self.position = position

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get or access private instance of 'position'."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set position to new tuple.

        Args:
            value: New tuple to update 'position'
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the current square area

        Returns:
            Current square area
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            # [print(" ", end="") for m in range(self.__position[0])]
            print(" " * self.__position[0] + "#" * self.__size)
