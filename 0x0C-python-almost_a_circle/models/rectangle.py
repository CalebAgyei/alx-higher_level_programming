#!/usr/bin/python3
"""Defines a class Rectangle that inherits from Base."""


from models.base import Base


class Rectangle(Base):
    """Represents a rectangle using Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle.

        Args:
            @width: Width of rectangle.
            @height: Height of rectangle.
            @x: x attribute of rectange.
            @y: y attribute of rectangle.
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """Accesses/gets private instance of width."""
            return (self.__width)

        @width.setter
        def width(self, value):
            """Sets or updates private instance attribute width."""
            self.__width = value

        @property
        def height(self):
            """Accesses or gets private instance attribute height."""
            return (self.__height)

        @height.setter
        def height(self, value):
            """Updates private instance attribute height."""
            self.__height = value

        @property
        def x(self):
            """Gets private instance attribute x."""
            return (self.__x)

        @x.setter
        def x(self, value):
            """Updates private instance attribute x."""
            self.__x = value

        @property
        def y(self):
            """Gets private instance attribute y."""
            return (self.__y)

        @y.setter
        def y(self, value):
            """Updates private instances attribute y with new value."""
            self.__y = value
