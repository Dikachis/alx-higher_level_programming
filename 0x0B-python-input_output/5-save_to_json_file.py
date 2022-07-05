#!/usr/bin/python3
"""
The "save_to_json_file" function container
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
