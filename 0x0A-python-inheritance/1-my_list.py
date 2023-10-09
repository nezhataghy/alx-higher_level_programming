#!/usr/bin/python3

'''Defines an inherited list class MyList'''


class MyList(list):
    '''Implements sorted printing for the built-in list class'''

    def print_sorted(self):
        '''Print a list in sorted ascending order'''
        list_copy = self[:]
        list_copy.sort()
        print(list_copy)
