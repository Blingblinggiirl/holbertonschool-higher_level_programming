#!/usr/bin/python3
""" Writing a Private instance attribute to class Square """


class Square():
    """ class that defines a square """

    def __init__(self, size=0):
        """ difine the size of the square """
        self.__size = size
