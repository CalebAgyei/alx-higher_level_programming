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

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""

        return self.__dict__
