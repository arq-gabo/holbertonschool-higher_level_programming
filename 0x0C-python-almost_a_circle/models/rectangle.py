#!/usr/bin/python3

"""Module Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor Class Method Init"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """Method width"""
            return self.__width

        @width.setter
        def width(self, width):
            """Method Setter Width"""
            self.__width = width

        @property
        def height(self):
            """Method height"""
            return self.__width

        @height.setter
        def height(self, height):
            """Method Setter Height"""
            self.__height = height

        @property
        def x(self):
            """Method x"""
            return self.__x

        @x.setter
        def x(self, x):
            self.__x = x

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, y):
            self.__y = y

            
