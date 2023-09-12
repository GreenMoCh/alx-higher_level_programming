#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """
    Defines a student with attributes
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representing of a student instance
        """
        return (self.__dict__)
