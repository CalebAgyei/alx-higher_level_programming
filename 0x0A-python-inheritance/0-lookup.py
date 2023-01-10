#!/usr/bin/python3
"""Defines an object attribute and method lookup function."""


def lookup(obj):
    """Returns the list of all available attributes and methods of an object.

    Args:
        @obj: object whose attributes and methods need to be listed
    """

    return (dir(obj))

if __name__ == "__main__":
    pass
