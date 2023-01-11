#!/usr/bin/python3
"""Defines a function class_to_join."""


import json


def class_to_json(obj):
    """Returns the dictionary description for JSON.
    Args:
        @obj: An instance of a Class.
    """

    return json.dumps(obj)
