#!/usr/bin/python3
"""Defines a class that inherits from list."""


class MyList(list):
    """Creates a class MyList."""


    my_list = []

    def print_sorted(self):
        """Prints sorted list in ascending order."""
        print(sorted(my_list))

