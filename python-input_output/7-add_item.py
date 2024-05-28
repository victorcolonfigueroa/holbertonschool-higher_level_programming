#!/usr/bin/python3
"""writes a script that adds all arguments to a Python list, and then save them to a file"""
import sys
import json


def save_to_json_file(my_obj, filename):
    """comment fucntion"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """comment fucntion"""
    with open(filename, 'r') as f:
        return json.load(f)


filename = "add_item.json"
try:
    items = load_from_json_file(filename)
except:
    items = []

for arg in sys.argv[1:]:
    items.append(arg)

save_to_json_file(items, filename)
