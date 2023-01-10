#!/usr/bin/python3
"""Defines a function that checks the instance of a specified class."""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class.

    Args:
        @obj: The object to check.
        @a_class: The class to match to the type of obj to."""

    if type(obj) == a_class:
        return True

    return False
