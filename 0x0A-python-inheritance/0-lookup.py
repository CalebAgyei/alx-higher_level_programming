#!/usr/bin/python3

def lookup(obj):
    """Returns the list of all available attributes and methods of an object.

    Args:
        @obj: object whose attributes and methods need to be listed
    """

    return list(dir(obj))

if __name__ == "__main__":
    pass