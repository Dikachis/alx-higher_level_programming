#!/usr/bin/python3
"""
script to save and load
"""
import sys

save_json = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    my_list = load_json(filename)
except (ValueError, FileNotFoundError):
    my_list = []
for args in sys.argv[1:]:
    my_list.append(args)
    save_json(my_list, filename)
