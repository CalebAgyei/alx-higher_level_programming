#!/usr/bin/python3
"""Defines a function save_to_json_file."""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation.

    Args:
        @my_obj: Python data structure (object) to write to text file.
        @filename: File to write object to.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return (json.dump(my_obj, f))
