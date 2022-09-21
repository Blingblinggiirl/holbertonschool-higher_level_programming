#!/usr/bin/python3
""" square with size, size must be an integer otherwise, error message """


class Square:
    """ size things """
    def __init__(self, size=0):
        if not isinstance(size, int):  # to indicate if is not an int
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
