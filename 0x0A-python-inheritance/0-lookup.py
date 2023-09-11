#!/usr/bin/python3
"""
Returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Return a list of available attributes and methods of an object

    Args:
        obj (object): The object to insert

    Returns:
        list: list of strs representing the atributes and methods
    """
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
