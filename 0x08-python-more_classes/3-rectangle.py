#!/usr/bin/python3
'''Defines a Rectangle class'''


class Rectangle:
    '''Represent a rectangle'''

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        '''width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        '''perimeter'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def area(self):
        '''area'''
        return (self.__width * self.__height)

    def __str__(self):
        '''String representation'''
        rectangle = ""
        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]
