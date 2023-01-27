#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    new_list.append(my_list)

    if idx < 0:
        return new_list
    if idx >= len(my_list):
        return new_list

    if my_list[idx] == element:
        new_list[idx] = element
    return new_list
