#!/usr/bin/python3
class Square:
    """
    class representing square
    This class defines a square with a private instance attribute

    Attributes:
        __size (int): the size of the square
    """
    def __init__(self, size=0):
        """
        initializes a new square instance

        Args:
            size (int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must ne an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        calculates the area of the square

        Returns:
            int: the area of the square
        """
        return (self.__size ** 2)
