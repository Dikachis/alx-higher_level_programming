#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list = []

    if idx < 0:
        return list
    if idx >= len(my_list):
        return list
    list = list(my_list)
    list[idx] = element
    return list
