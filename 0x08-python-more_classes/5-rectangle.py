#!/usr/bin/python3
""" Defines a Rectangle. """


class Rectangle:
    """ Represents a Rectangle. """

    def __init__(self, width=0, height=0):
        """" Initialize a new rectangle
        
        Args:
            width (int): the width
            heigth (int): the height
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """ Set the width of the rectangle """
        return (self.__width)
    
    @width.setter
    def width(self, value):
        if not isinstance(value,int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Set the height of the rectangle """
        return (self.__height)
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Return the area of the rectangle"""
        return (self.__width * self.__height)
    
    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))
    
    def __str__(self):
        """Return Print the rectangle
        
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle_str = []
        for i in range(self.__height):
            [rectangle_str.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle_str.append("\n")
        return ("".join(rectangle_str))
    
    def __repr__(self):
        """Return the string repr of the rectangle."""
        rectangle_str = "Rectangle(" + str(self.__width)
        rectangle_str += ", " + str(self.__height) + ")"
        return (rectangle_str)
    
    def __del__(self):
        """Print a deletation message of a rectangle"""
        print("Bye rectangle...")