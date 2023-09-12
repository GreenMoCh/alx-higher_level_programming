#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """
    Convert an instance of a class into a dictionary for JSON serialization
    """
    return (obj.__dict__)
