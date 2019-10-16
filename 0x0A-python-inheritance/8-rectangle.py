#!/usr/bin/python3
class BaseGeometry:
    """Class BaseGeometry for a method with public instance"""
    pass

    def area(self):
        """method for area public instance"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method for validate the argument name"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """"""
    def __init__(self, width, height):
        """"""
        BaseGeometry.integer_validator(self, width, height)
        BaseGeometry.integer_validator(self, width, height)
        self.__width = width
        self.__height = height
