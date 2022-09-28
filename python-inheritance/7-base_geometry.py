#!/usr/bin/python3
"""task 7 """


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """raise an exception of a geometry area"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """validates if value is an int or not"""
        if not isinstance(value, int):
            raise TypeError(value + " must be an integer")
        if value <= 0:
            raise ValueError(value + " must be greater than 0")
