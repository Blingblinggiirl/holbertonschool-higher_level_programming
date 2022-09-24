#!/usr/bin/python3
""" function that adds two integers """


def add_integer(a, b=98):
    """ is not int or float, error """
    if (int(a), int(b)):
        return a + b
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    elif (a is not isinstance(a, int) or (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    elif (b is not isinstance(b, int) or (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    elif (a == 0) or (b == 0):
        raise TypeError("a and/or b missing")
    return int(a) + int(b)
