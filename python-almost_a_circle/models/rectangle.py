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
    """to getter"""

    def width(self):
        return self.__width

    @width.setter
    """to setter"""

    def width(self, value):
        self.__width = value
        if width isinstance != int:
            raise TypeError("width must be an integer")
        if width is <= 0:
            raise ValueError("width must > 0")

    @property
    """ to getter """

    def height(self):
        return self.__height

    @height.setter
    """ to  setter """

    def height(self, value):
        self.__height = value
        if height isinstance != int:
            raise TypeError("height must be an integer")
        if height is <= 0:
            raise ValueError("height must be > 0")

    @property
    """ to getter """

    def x(self):
       return self.__x

    @x.setter
    """ to setter """
    
    def x(self, value):
        self.__x = value
        if x isinstance != int:
            raise TypeError("x must be an integer")
        if x is not >= 0:
            raise ValueError("x must be >= 0")

    @property
    """ to getter """
    
    def y(self):
       return self.__y

    @y.setter
    """ to setter """
    
    def y(self, value):
        self.__y = value
        if y isinstance != int:
            raise TypeError("y must be an integer")
        if y is not >= 0:
            raise ValueError("y must be >= 0")
