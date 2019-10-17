#!/usr/bin/python3

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits methods of class BaseGeometry"""
    def __init__(self, width, height):
        """Method for validate values of with and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method for calculate the reactangule area"""
        return self.__width * self.__height

    def __str__(self):
        """return string message"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """Muper init for change value width an height for size"""
        self.__size = size
        super().__init__(self.__size, self.__size)
