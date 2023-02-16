#!/usr/bin/python3
""" Rectangule using Base """
from models.base import Base


class Rectangle(Base):
    """ Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
	if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
        super().__init__(id)
