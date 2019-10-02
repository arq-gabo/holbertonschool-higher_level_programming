#!/usr/bin/python3
class Square:
    """Create Class"""
    pass

    def __init__(self, size=0):
        """Create Atribute for Class Square whit Init Method"""
        self.__size = size

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return(self.__size**2)
