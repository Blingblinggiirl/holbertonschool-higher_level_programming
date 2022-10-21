#!/usr/bin/python3
""" rectangle """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ setter """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ setter """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ setter """
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ setter """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ return the area value of the Rectangle instance """
        return self.__width * self.__height

    def display(self):
        """ display # """
        for i in range(self.__y):
            print()
        for height in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for width in range(self.width):
                if width == self.__width - 1:
                    print("#")
                else:
                    print("#", end="")

    def __str__(self):
        """ str reppp"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} " +
                f"- {self.__width}/{self.__height}")
