#!/usr/bin/python3
"""class Square."""


class Square:
    """square content"""
    def __init__(self, size=0):
        self.__size = size

    """getter"""
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ current square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square"""
        print("#")
        if self.__size == 0:
            print()
        else:
            for side_a in range(self.__size):
                for side_b in range(self.__size):
                    print("#", end="")
                print()
