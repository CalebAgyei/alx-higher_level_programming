#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Creates an class BaseGeometry."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer.

        Args:
            @name: Name of parameter
            @value: Parameter to validate"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
