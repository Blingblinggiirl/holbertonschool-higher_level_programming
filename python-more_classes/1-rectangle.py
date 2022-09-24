#!/usr/bin/python3
""" class rectangle that define a rectangle """


class Rectangle:
    """ rectangle """
    
    def __init__(self, width, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set"""
        if isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

