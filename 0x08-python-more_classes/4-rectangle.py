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
        return (self.width * self.height)
    
    def perimeter(self):
        """Return the perimeter of the rectangle"""
        return (2 * (self.width + self.height))
    
    def __str__(self):
        """Print the recc=angle"""
        if self.width == 0 or self.height == 0:
            return ("")
        else:
            rectangle_str = ""
            for _ in range(self.height):
                rectangle_str += "#" * self.width + "\n"
            return (rectangle_str[:-1])
    
    def __repr__(self):
        """"Return the string rep of the rectangle"""
        return (f"Rectangle({self.width}, {self.height})")