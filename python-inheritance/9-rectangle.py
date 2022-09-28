#!/usr/bin/python3
"""task 9 """


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """raise an exception of a geometry area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if value is an int or not"""
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")

class Rectangle(BaseGeometry):
    """Class that define a new class based on BaseGeometry class"""

    def __init__(self, width, height):
        """To create a new instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """get are of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        module = f"[Rectangle] {self.__width}/{self.__height}"
        return module

