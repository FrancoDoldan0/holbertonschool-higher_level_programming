#!/usr/bin/python3
"""
    defines an add function
    The test is located in the tests folder

"""


def add_integer(a, b=98):
    """
    adds two integers unless they are floats,
    """
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    c = a + b
    return (c)
