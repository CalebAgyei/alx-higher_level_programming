#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Creates an class BaseGeometry."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""Defines a class Rectangle."""


class Rectangle(BaseGeometry):
    """Creates a class Rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a rectangle.

        Args:
            @width: Width of rectangle.
            @height: Height of rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
