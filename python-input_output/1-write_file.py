#!/usr/bin/python3
"""     task 1: write a string to text file and
        return num of chars
"""


def write_file(filename="", text=""):
    """ UTF8 and numb of chars """
    with open(filename, 'w', encoding='UTF-8') as file:
        return file.write(text)
