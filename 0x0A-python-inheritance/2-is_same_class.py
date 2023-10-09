#!/usr/bin/python3
"""Defines a class-checking function"""


def is_same_class(obj, a_class):
    """ Function that returns True/False if obj is an instance of a_class
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be of type 'type'")
    return (type(obj) is a_class)
