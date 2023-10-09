#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """extended version of list
    """

    def print_sorted(self):
        """prints the list sorted
        """
        my_list = self[:]
        my_list.sort()
        print(my_list)
