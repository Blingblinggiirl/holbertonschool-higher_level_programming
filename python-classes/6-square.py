#!/usr/bin/python3
"""
    class Square 
"""


class Square:
    """ define a square """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self, value):
        """ getter size """
        return self.__size

    @size.setter
    def size(self,value):
        if not isinstance(value, int):
            raise TypeError("size mustbe be an integer")
        if value < 0:
            raise ValueError("size must be > 0")
        self.__size = value

    def area(self):
        """get the area of the square """
        return(self.__size * self.__size)
    
    def my_print(self):
        """ time to print th square """
        if self.__size > 0:
            for i in range(0, self.__position[1]):
                print()

            for x in range(0, self.__size):
                for i in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
        if self.__size == 0:
            print()
