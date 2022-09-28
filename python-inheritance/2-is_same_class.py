#!/usr/bin/python3
"""Return True if obj is exactly an instance of a specified class, false otherwise"""


def is_same_class(obj, a_class):
    """rwturs Trye or false depending if is instance"""
    return issubclass(a_class, type(obj))
