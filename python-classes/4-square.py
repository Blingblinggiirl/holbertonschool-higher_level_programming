#!/usr/bin/python3
""" Writing a Private instance attribute to class Square """


class Square():
    """ class that defines a square """

    def __init__(self, size=0):
        """ difine the size of the square """
        self.__size = size

    @property
    def size(self):
        """ inicializando size """
        self.__size

    @size.setter
    def size(self, value):
        """ to set """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ area """
        return self.__size * 2
