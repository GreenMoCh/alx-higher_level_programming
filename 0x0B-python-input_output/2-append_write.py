#!/usr/bin/python3
"""Append to file"""


def append_write(filename="", text=""):
    """
    Append a str to the end of the text file and return the number of chars written
    """
    with open(filename, "a", encoding="utf-8") as File:
        num_chars_added = File.write(text)
    return (num_chars_added)
