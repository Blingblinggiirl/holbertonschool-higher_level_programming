#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copyofmy_list = my_list.copy()
    if idx < 0 or idx > len(my_list):
        return copyofmy_list
    else:
        copyofmy_list[idx] = element
        return copyofmy_list
