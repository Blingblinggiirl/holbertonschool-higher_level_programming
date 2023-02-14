#!/usr/bin/python3
    """
        making a Square.
    """

class Square:
    """ define a square """

    def __init__(self, width):
        """ to init """

        self._width = width

    @property
    def width(self):
        """ to get width """
        return self._width

    @width.setter
    def width(self, value):
	""" to set """
	
	if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value



