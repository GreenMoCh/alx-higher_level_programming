#!/usr/bin/python3
"""
this module cheks if an ibject is an instance of the specific class
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of the specific class

    Args:
        obj: the object to check
        a_class: the class to compare against

    Returns:
        bool: True or False
    """
    return (type(obj) is  a_class)
