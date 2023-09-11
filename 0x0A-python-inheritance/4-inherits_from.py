#!/usr/bin/python3
"""Cheks if an obj is an instance of class"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of class

    Args:
        obj: the object to check
        a_class: The class to compare to

    Returns:
        bool: True or False
    """
    return (isinstance(obj,a_class) and type(obj) is not a_class)
