#!/usr/bin/python3
"""Defines a class student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes student.


        Args:
            @first_name: Student's first name
            @last_name: Student's last name
            @age: Age of student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            @attrs: Attributes to be used"""

        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            @json: Dictionary.
        """

        for x, y, in json.items():
            setattr(self, k, v)
