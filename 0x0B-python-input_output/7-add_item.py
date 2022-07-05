#!/usr/bin/python3
"""
script to save and load
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
my_list = []

try:
    my_list = load_from_json_file(filename)
except Exception:

arg_len = len(argv)

if arg_len > 1:
    for i in range(1, arg_len):
        my_list.append(argv[i])

    save_to_json_file(my_list, filename)
