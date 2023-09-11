#!/usr/bin/python3
"""
Print the list in ascending sorted order
"""


class MyList(list):
    """ Class that inherits list"""
    def print_sorted(self):
        """
        Print the list in ascending sorted order
        """
        print(sorted(self))
