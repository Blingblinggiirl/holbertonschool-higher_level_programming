#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    return [element if item == idx else item for item in my_list]
