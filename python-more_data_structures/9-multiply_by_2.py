#!/usr/bin/python3
def multiply_by_2(dic):
    mod = {}
    if dic != None:
        for key, value in dic.items():
            mod[key] = value*2
    return mod
