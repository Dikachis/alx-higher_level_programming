#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for a in a_dictionary:
            if a == key:
                a_dictionary[a] = value
    return a_dictionary
