#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list.sort()
    if my_list is None:
        return None
    elif len(my_list) > 0:
        return my_list[-1]
