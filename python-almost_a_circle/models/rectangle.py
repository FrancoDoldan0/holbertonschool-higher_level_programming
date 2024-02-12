#!/usr/bin/python3
"""rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """getters"""
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def y(self):
        return self.__y

    @property
    def x(self):
        return self.__x

    """setters"""
    @width.setter
    def width(self, value):
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value

    @y.setter
    def y(self, value):
        self.__y = value

    @x.setter
    def x(self, value):
        self.__x = value
