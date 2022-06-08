#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for idx, item in enumerate(my_list):
        if item == search:
            myl[idx] = replace
    print(my_list)
