#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    for idx in my_list:
        new_list = idx.replace("my_list[idx]", "new_element")
        return (new_list)
