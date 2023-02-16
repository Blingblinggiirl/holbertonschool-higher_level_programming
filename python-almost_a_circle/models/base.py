#!/usr/bin/python3
""" is a base for other classes """


class Base:
    """ class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ defines a private class attribute """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
