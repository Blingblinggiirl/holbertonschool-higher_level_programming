#!/usr/bin/python3
""" Writing a Private instance attribute to class Square """


class Square():
    """ class that defines a square """

    def __init__(self, size=0):
        """ difine the size of the square """
        self.__size = size
        
        if size is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")