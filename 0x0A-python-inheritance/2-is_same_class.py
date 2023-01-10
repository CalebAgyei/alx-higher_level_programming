#!/usr/bin/python3
"""Defines a function that checks the instance of a specified class."""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class."""

    if not isinstance(obj, a_class):
        return False

    return (True)
