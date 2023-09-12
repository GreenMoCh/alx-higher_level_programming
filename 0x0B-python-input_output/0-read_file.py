#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """
    Read a text file UTF8 and print its content to stdout
    """
    with open(filename, "r", encoding="utf-8") as File:
        print(File.read(), end="")
