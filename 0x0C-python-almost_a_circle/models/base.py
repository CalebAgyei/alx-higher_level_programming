#!/usr/bin/python3
"""Defines a class Base."""


class Base:
    """
    Serves as the base of all other classes in project.
    Manages id attribute in all future clases and avoid duplicating
    codes and bugs.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base class.

        Args:
            @id: Identity of class.
        """

        self.id = id

        if self.id is not None:
            self.id = self.id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
