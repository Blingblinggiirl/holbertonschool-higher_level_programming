#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    maxnum = None
    for idx in my_list:
        if maxnum is None or maxnum < idx:
            maxnum = idx
        return(maxnum)
