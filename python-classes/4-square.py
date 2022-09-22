#!/usr/bin/python3
""" class squarethat defines a square """


class Square:
    """ class Square """
    def __init__(self, size=0):
        self.__size = size
        
    @property
    def size(self):
        """ size """
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be > 0")
        self.__size = value
        
    def area(self):
        """ area """
        return (self.__size * self.__size)
