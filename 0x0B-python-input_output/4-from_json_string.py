#!/usr/bin/python3
"""Defines a function from_json_string."""


import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by
            a JSON string (my_str)."""

    return (json.loads(my_str))
