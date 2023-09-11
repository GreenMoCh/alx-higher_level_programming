#!/usr/bin/python3
"""Defines a rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represant a square"""

    def __init__(self, size):
        """Represent a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
