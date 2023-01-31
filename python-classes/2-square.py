#!/usr/bin/python3
""" Class Square with size validation """


class Square():
    """ class that defines a square """

    def __init__(self, size=0):
        """ difine the size of the square """
        self.__size = size
        if size not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")

