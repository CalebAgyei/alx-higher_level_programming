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
            if type(value) != int:
                raise TypeError("width must be an integer")
            elif value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """Accesses or gets private instance attribute height."""
            return (self.__height)

        @height.setter
        def height(self, value):
            """Updates private instance attribute height."""
            if type(value) != int:
                raise TypeError("height must be an integer")
            elif value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """Gets private instance attribute x."""
            return (self.__x)

        @x.setter
        def x(self, value):
            """Updates private instance attribute x."""
            if type(value) != int:
                raise TypeError("x must be an integer")
            elif value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """Gets private instance attribute y."""
            return (self.__y)

        @y.setter
        def y(self, value):
            """Updates private instances attribute y with new value."""
            if type(value) != int:
                raise TypeError("y must be an integer")
            elif value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):
            """Returns area of Rectangle."""
            return (self.__width * self.__height)
