#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """
    Defines a student with attribute
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of student instance
        """
        if attrs is None:
            return (self.__dict__)
        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return (result)
