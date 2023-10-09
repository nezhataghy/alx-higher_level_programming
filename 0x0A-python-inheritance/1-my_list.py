#!/usr/bin/python3
""" my list"""


class MyList(list):
    """extended version of list
    """

    def print_sorted(self):
        """prints the list sorted
        """
        my_list = self[:]
        my_list.sort()
        print(my_list)
