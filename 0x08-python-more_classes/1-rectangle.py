#!/usr/bin/python3

"""Defines a class rectangle."""


class Rectangle:
    """Empty class that defines a rectangle.

    Args:
        @width: width of rectangle
        @height: height of rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Access private instance attribute of 'width'."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets private instance of width to a new value.

        Args:
            @value: new value for width.
            """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Access private instance attribute of 'height'."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets private instance of height to a new value.

        Args:
            @value: new value for height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


if __name__ == "__main__":
    pass
