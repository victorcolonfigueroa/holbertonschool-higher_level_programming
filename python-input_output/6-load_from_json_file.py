#!/usr/bin/python3
"""loads an object from a JSON file"""
import json


def load_from_json_file(filename):
    """writes an object to a text file, using a JSON representation"""
    with open(filename, encoding="utf-8") as fd:
        return json.load(fd)
