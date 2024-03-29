#!/usr/bin/python3
"""class Square."""


class Square:
    """square content"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ current square area"""
        return self.__size * self.__size
