#!/usr/bin/python3
"""To JSON string"""
import json


def to_json_string(my_obj):
    """
    Convert an object to ist JSON representation as a str
    """
    return (json.dumps(my_obj))
