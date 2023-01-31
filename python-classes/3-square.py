#!/usr/bin/python3
""" Writing a Private instance attribute to class Square """


class Square():
    """ class that defines a square """
    def __init__(self, size=0):
        """ difine the size of the square """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area of a square"""
        return .__size * 2
