#!/usr/bin/python3
class Rectangle:

    def __init__(self, width=0, height=0):
        """Create Atribute for Class Rectangle with Init Method"""
        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            self.__height = value
            if value < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            self.__width = value
            if value < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    def area(self):
        return(self.__width * self.__height)

    def perimeter(self):
        if self.width is 0 or self.height is 0:
            return(0)
        else:
            return((self.__width * 2) + (self.__height * 2))
