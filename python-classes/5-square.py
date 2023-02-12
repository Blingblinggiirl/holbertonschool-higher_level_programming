#!/usr/bin/python3
"""Class Square"""


class Square:
    """square"""

    def __init__(self, size=0):
        """This init a  class"""
        self.size = size

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """ this should print a # in the area """

        if self.__size == 0:
            print("")

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
