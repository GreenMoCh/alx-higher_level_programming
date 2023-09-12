#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """
    Write a string to a text file utf-8 and return the number of chars written
    """
    with open(filename, "w", encoding="utf-8") as File:
        num_chars_written = File.write(text)
    return (num_chars_written)
