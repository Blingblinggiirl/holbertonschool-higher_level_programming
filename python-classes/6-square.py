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
    def size(self):
        """ getter size """
        return self.__size

    @size.setter
    def size(self,value):
        if not isinstance(value, int):
            raise TypeError("size mustbe be an integer")
        if value < 0:
            raise ValueError("size must be > 0")
        self.__size = value

    @property
    def position(self):
        """getter position """
        return self.__position

    @position.setter
    def position(self, value):
        """set position"""
        if type(value) != tuple or len(value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """get the area of the square """
        return(self.__size * self.__size)

    def my_print(self):
        """Prints the square with the # character"""
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
    
