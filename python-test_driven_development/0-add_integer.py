#!/usr/bin/python3
""" function that adds two integers """


def add_integer(a, b=98):
    """ is not int or float, error """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    elif (a == 0) or (b == 0):
        raise TypeError("a and/or b missing")
    if (int(a), int(b)):
        return a + b
    return int(a) + int(b)
