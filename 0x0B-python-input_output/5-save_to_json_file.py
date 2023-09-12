#!/usr/bin/python3
"""Save object to file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation
    """
    with open(filename, "w") as File:
        json.dump(my_obj, File)
