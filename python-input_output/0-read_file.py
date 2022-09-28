#!/usr/bin/python3
"""     Task 0      """


def read_file(filename=""):
    """ reads a UTF 8 and print it """
    with open(filename, 'r', encoding='UTF-8') as file:
        print(file.read(), end="")
