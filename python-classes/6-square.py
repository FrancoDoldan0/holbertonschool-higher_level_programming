#!/usr/bin/python3
"""class Square."""


class Square:
    """square content"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    """getter"""
    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ current square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square"""
        if self.__size == 0:
            print()
        else:
            for h in range(self.position[1]):
                print()
            for side_a in range(self.__size):
                for h in range(self.position[0]):
                    print(" ", end="")
                for side_b in range(self.__size):
                    print("#", end="")
                print()
