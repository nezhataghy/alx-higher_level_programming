#!/usr/bin/python3
'''Defines a Rectangle class'''


class Rectangle:
    '''Represent a rectangle'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
            rectangle += (str(self.print_symbol) * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        '''string representation of the rectangle
          to be able to recreate a new instance'''
        rep = "{}({}, {})".format(self.__class__.__name__,
                                  self.width, self.height)
        return rep

    def __del__(self):
        '''Detect instance deletion'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Method that returns the bigger Rectangle'''

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''Creates a Rectangle instance
          where width and height are size'''
        return (cls(size, size))
