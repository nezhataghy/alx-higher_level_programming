#!/usr/bin/python3
"""Defines a class-checking function"""


def is_kind_of_class(obj, a_class):
    """ Function that returns True/False if obj is an instance of a_class
    """
    return isinstance(obj, a_class)
