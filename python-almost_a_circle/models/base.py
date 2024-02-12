#!/usr/bin/python3
"""Base class"""


class Base:
    """private atr"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is None:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
