#!/usr/bin/python3
"""class Rectangle."""


class Rectangle:
    """void class"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """width getter"""
    @property
    def width(self):
        return self.__width

    """width setter"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """heigth getter"""
    @property
    def height(self):
        return self.__height

    """height setter"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """methods"""
    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):

        rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for sidea in range(self.__height):
            rectangle = rectangle + ("#" * self.__width + '\n')
        return rectangle[:-1]

    def __repr__(self):
        return ("{}, {}".format(self.__width, self.__height))
