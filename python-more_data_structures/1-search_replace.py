#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mol = []
    if my_list != None:
        mol = list(map(lambda e: replace if e == search else e, my_list))
    else:
        return None
    return mol
