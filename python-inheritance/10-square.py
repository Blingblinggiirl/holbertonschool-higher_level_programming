#!/usr/bin/python3
"""Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class based on Rectangle"""

    def __init__(self, size):
        """create a new instance"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Area of a square"""
        return self.__size * self.__size
