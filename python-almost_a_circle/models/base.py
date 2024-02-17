#!/usr/bin/python3
"""Base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return json.dumps(list_dictionaries)
