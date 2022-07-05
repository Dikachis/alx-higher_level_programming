#!/usr/bin/python3
"""
script to save and load
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except Exception:
    my_list = []
for sys.args in sys.argv[1:]:
    my_list.append(sys.args)
    save_to_json_file(my_list, filename)
