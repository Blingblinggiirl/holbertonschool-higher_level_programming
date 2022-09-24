#!/usr/bin/python3
""" function that adds two integers """


def add_integer(a, b=98):
    """ is not int or float, error """
    if (a is not isinstance(a, int) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (b is not isinstance(b, int) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    if (a == 0) or (b == 0):
        raise TypeError("a and/or b missing")
    return int(a) + int(b)
