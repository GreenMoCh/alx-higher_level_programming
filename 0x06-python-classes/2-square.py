#!/usr/bin/python3
class Square:
    """
    class representing a square
    This class defines with a private instance attribute

    Attributes:
        __size (int): the size of the square
    """
    def __init__(self, size=0):
        """
        Initializes a new square instance

        Args:
            size (int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
