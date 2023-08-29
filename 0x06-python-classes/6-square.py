#!/usr/bin/python3
class Square:
    """
    class representing a square
    This class defines a square with private instance attributes

    Attributes:
        __size (int): the size of the square
        __position (tuple): the position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        initializes a new square instance

        Args:
           size (int): the size of the square
           position (tuple): the position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square

        Returns:
            int: the size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set the size of the square

        Args:
            value (int): the new size value

        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square

        Returns:
            tuple: the position of the square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Set the position of the square

        Args:
            value (tuple): the new position value

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(v, int) and v <= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
