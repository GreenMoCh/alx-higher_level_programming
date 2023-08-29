#!/usr/bin/python3
class Square:
    """
    A class representing a square
    This class defines a squae with a private instance attribute

    Attributes:
        __size (int): the size of the square
    """
    def __init__(self, size=0):
        """
        Initializes a new square instance

        Args:
            size (int): the size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square

        Returns:
            int: the size of the square
        """
        return (self.size)

    @size.setter
    def size(self, value):
        """
        Set size of the square

        Args:
            value (int): the ne size value

        Raises:
            TypeError: If the value is not an integer
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

    def my_print(self):
        """
        Prints the square using the '#' character

        If size is 0, an empty line is printed
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
