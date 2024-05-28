#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads and prints the contents of a file.


    """
    with open(filename, encoding="utf-8") as fd:
        """Prints the contents of the file."""
        for line in fd:
            print(line, end="")
