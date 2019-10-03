#!/usr/bin/python3
class Square:
    """Create Class"""

    def __init__(self, size=0):
        """Create Atribute for Class Square whit Init Method"""
        self.size = size

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, value):
        """"Exception Error"""
        if type(value) is int or type(value) is float:
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Function for find the area square"""
        return(self.__size**2)

    def __lt__(self, value_new):
        """comparison method less"""
        return self.area() < value_new.area()

    def __le__(self, value_new):
        """comparison method equal-less"""
        return self.area() <= value_new.area()

    def __eq__(self, value_new):
        """comparison method equal"""
        return self.area() == value_new.area()

    def __ne__(self, value_new):
        """comparison method different"""
        return self.area() != value_new.area()

    def __gt__(self, value_new):
        """major comparison method"""
        return self.area() > value_new.area()

    def __ge__(self, value_new):
        """major-equal comparison method"""
        return self.area() >= value_new.area()
