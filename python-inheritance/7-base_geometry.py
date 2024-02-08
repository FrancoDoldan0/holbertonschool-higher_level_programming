#!/usr/bin/python3
"""Improve Geometry"""


class BaseGeometry:
    """Raise exp"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError("{} {}".format(name, "must be an integer"))
        if value <= 0:
            raise ValueError("{} {}".format(name, "must be greater than 0"))
