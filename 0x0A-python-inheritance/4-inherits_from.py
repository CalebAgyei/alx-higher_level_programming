#!/usr/bin/python3
"""Defines a function that checks if object is a subclass."""


def inherits_from(obj, a_class):
    """Returns True if obj is a subclass

    Args:
        @obj: The object to check.
        @a_class: The specified class to match to obj to.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True

    return False
