#!/usr/bin/python3
"""Class Student that defines a student """


class Student:
    """Class student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json"""
        listt = {}
        self_dict = self.__dict__

        if attrs is None:
            return self_dict
        elif type(attrs) is list:
            for i in attrs:
                if hasattr(self, i):
                    listt[i] = getattr(self, i)
            return listt

