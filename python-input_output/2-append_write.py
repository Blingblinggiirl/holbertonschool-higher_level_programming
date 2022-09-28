#!/usr/bin/python3
"""     Task 2      """


def append_write(filename="", text=""):
    """ to return number of chars added """
    with open(filename, 'a', encoding='utf-8') as file_create:
                return file_create.write(text)
