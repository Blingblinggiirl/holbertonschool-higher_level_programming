#!/usr/bin/python3
"""My list that inherits from list"""


class MyList(list):
    """ Mylist inherits from list"""
    def print_sorted(self):
        """printea la lista ya sorteada"""
        print(sorted(self))
