#!/usr/bin/python3
"""Create object from JSON file"""
import json


def load_from_json_file(filename):
    """
    Load an object from JSON file and return the corresponding python object
    """
    with open(filename, "r") as File:
        return (json.load(File))
