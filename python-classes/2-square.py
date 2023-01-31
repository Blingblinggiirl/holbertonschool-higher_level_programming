#!/usr/bin/python3
i


class Square:
    """Square with size validation
    """
    def __init__(self, size=0):
        """ init
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
	if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
