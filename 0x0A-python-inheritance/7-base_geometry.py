#!/usr/bin/python3
"""Base Geometry class"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """Raise an exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the given int value and raise exceptions

        Args:
            name (str): The name of the value
            value: the value to be validated

        Raises:
            TypeError: If the value is not an int
            ValueError: If the value <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
