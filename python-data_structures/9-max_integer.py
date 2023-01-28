#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    maxnum = my_list[0]
    for idx in my_list:
        if maxnum is None or maxnum < idx:
            maxnum = idx
    return maxnum
