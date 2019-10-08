#!/usr/bin/python3

"""
Rectangle
"""


class Rectangle:
    """Class rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Create Atribute for Class Rectangle with Init Method"""
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def height(self):
        """Method for check height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method for check exception error"""
        if type(value) is int:
            self.__height = value
            if value < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """Method for check width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method for check exception error"""
        if type(value) is int:
            self.__width = value
            if value < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    def area(self):
        """Method for calculate the area """
        return(self.__width * self.__height)

    def perimeter(self):
        """Method for calculate the perimeter"""
        if self.width is 0 or self.height is 0:
            return(0)
        else:
            return((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Method to build the string with the "#" character"""
        if self.width is 0 or self.height is 0:
            return(0)
        else:
            new_str = ""
            for a in range(self.__height):
                new_str += str(self.print_symbol) * self.width
                if a + 1 < self.height:
                    new_str += '\n'
        return new_str

    def __repr__(self):
        """Method for representation an intance of the square"""
        a = str(self.__width)
        b = str(self.__height)
        new_repr = "Rectangle(" + a + ", " + b + ")"
        return(new_repr)

    def __del__(self):
        """Method del for delete instances"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
