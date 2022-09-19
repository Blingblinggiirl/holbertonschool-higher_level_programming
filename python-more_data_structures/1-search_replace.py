#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mol = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            mol.append(replace)
        else:
            mol.append(my_list[i])
        return mol
