#!/usr/bin/python3
"""
    class rectangle that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """ Rectangle """

    def __init__(self,width, height, x=0, y=0, id=None):
        """init with super init so i can use thing initialized in Base """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        self.__width = value
        if width isinstance != int:
            raise TypeError("width must be an integer")
        if width is <= 0:
            raise ValueError("width must > 0")

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        self.__height = value
        if height isinstance != int:
            raise TypeError("height must be an integer")
        if height is <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """getter"""
       return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        self.__x = value
        if x isinstance != int:
            raise TypeError("x must be an integer")
        if x is not >= 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """getter"""
       return self.__y

    @y.setter
    def y(self, value):
        """getter"""
        self.__y = value
        if y isinstance != int:
            raise TypeError("y must be an integer")
        if y is not >= 0:
            raise ValueError("y must be >= 0")
