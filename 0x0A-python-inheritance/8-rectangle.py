#!/usr/bin/python3
"""Base Geometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new rect"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
