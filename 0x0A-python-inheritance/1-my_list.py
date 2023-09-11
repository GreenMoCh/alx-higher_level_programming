#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        """
        Print the list in ascending sorted order
        """
        sorted_list = sorted(self)
        for item in sorted_list:
            print(item, end=" ")
        print()
