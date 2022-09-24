#!/usr/bin/python3
""" function that adds two integers """


def add_integer(a, b=98):
    """ is not int or float, error """
    if (int(a), int(b)):
        return a + b
    elif (a is not isin0stance(a, int) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    elif (b is not isinstance(b, int) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    elif (a == 0) or (b == 0):
        raise TypeError("a and/or b missing")
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
