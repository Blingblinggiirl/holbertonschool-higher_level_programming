#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Defines a rectangle by width and height
    """
    def __init__(self, width=0, height=0):
        """
        init method
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter width"""
        return self.__width

    @property
    def height(self):
        """ getter height"""
        return self.__height

    @width.setter
    def width(self, value):
        """ setter width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

