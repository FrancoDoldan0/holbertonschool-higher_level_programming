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

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string to file"""
        if list_objs is None:
            list_objs = []
        file = f"{cls.__name__}.json"
        with open(file, 'w') as f:
            json_string = (cls.to_json_string([obj.to_dictionary()
                                               for obj in list_objs]))
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or (json_string) == '':
            return ("[]")
        else:
            return json.loads(json_string)
