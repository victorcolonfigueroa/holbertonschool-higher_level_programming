#!/usr/bin/python3
"""returns an object (Python data structure) represented by a JSON string"""
import json


import json

def from_json_string(my_str):
    """Converts a JSON string representation into a Python object."""
    return json.loads(my_str)
