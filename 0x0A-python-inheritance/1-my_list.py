#!/usr/bin/python3

'''Defines an inherited list class MyList'''


class MyList(list):
    '''Implements sorted printing for the built-in list class'''

    def print_sorted(self):
        '''Method that prints the sorted list'''
        list_sorted = self.copy()
        list_sorted.sort()
        print(list_sorted)
