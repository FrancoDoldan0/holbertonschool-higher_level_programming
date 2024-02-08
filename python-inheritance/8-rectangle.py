#!/usr/bin/python3
"""class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Rectangle function"""
        self.__width = width
        super().integer_validator("width", width)
        self.__height = height
        super().integer_validator("height", height)
