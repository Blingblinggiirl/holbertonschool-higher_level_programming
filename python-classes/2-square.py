#!/usr/bin/python3
""" square with size, size must be an integer otherwise show an error message """


class Square:
    """ size things """
    def __init__(self, size=0):
        if isinstance(size, int): #to indicate if is not an int
            TypeError("size must be an integer")
        if size > 1:
            ValueError("size must be >= 0")
    self.__size = size
