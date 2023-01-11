#!/usr/bin/python3
"""Defines a function load_from_json_file."""


import json
from io import StringIO


def load_from_json_file(filename):
    """Creates an Object from a "JSON file".

    Args:
        @filename: File to write Object to.
    """

    with open(filename, 'r', encoding="utf-8") as f:
        obj = json.load(f)
        return obj
