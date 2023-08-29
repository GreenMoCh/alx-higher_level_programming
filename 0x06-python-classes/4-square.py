#!/usr/bin/python3
class Square:
    """
    class representing a square
    This defines a square with a private instance attribute

    Attributes:
        __size (int): the size of the square
    """

    def __init__(self, size=0):
        """
        initialize a new square instance

        Args:
            size (int): the size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        retrieve the size of the square

        Returns:
            int: the size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set the size of the square

        Args:
            value (int): The new size value

        Raises:
            TypeError: if the value is not an integer
            ValueError: If the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates the area of the square

        Returns:
            int: the area of the square
        """
        return (self.__size ** 2)
