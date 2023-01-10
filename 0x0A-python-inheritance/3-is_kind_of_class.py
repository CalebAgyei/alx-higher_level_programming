#!/usr/bin/python3
"""Defines a function that checks if object is an instance of \
        "or if object is an instance of a class that inherited \
        "from, the specified class."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class.

    Args:
        @obj: The object to check.
        @a_class: The specified class to match to obj to.
    """
    
    if isinstance(obj, a_class):
        return True

    return False
