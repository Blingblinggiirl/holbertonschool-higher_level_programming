#!/usr/bin/python3
"""
    class rectangle that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """ Rectangle """
    @property 
    def width(self):
        self.__width
    
    @width.setter
    def width(self, value):
        self.__width = width

    @property
    def height(self):
        self.__height
    
    @height.setter
    def height(self, value):
        self.__height = height

    @property
    def x(self):
        self.__x

    @x.setter
    def x(self, value):
        self.__x = x

    @property
    def y(self):
        self.__y
    
    @y.setter
    def y(self, value):
        self.__y = y
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
