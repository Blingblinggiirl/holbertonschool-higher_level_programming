#!/usr/bin/python3
"""task 8"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Define a new task based on BaseGeometry """

    def __init__(self, width, height):
        """new class defined based on BaseGeometry"""
	self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
