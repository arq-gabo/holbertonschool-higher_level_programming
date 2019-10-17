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
        """Super init for change value width an height for size"""
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Return string message"""
        return "[Square] {}/{}".format(self.__size, self.__size)
