#!/usr/bin/python3

def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file and returns the number of characters written."""
    
    with open(filename, mode="a", encoding="utf-8") as fd:
        """append text to the file."""
        fd.write(text)
    return len(text)
