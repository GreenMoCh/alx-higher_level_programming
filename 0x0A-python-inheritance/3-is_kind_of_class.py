#!/usr/bin/python3
"""Cheks if an abject is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is instance of class

    Args:
        obj: the object to check
        a_class: the class to compare to

    Returns:
        bool: True or False
    """
    return (isinstance(obj, a_class))
