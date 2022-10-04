#!/usr/bin/python3
""" Creating an class called base """


class Base:
    """Class base:
    private class attribute __nb_objects
    class constructor: init(self, id=None)
        """
    __nb_objects = 0
    def __init__(self, id=None):
        """Initializing Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nd_objects
