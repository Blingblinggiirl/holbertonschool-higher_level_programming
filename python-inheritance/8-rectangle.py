#!/usr/bin/python3
""" Rectancle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Define a new task based on BaseGeometry """

    def __init__(self, width, height):
        """New class defined based on BaseGeometry"""
	self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
