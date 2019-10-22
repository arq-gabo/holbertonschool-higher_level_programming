#!/usr/bin/python3


"""Module Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Method init for constructor class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Method size"""
        return self.width

    @size.setter
    def size(self, size):
        """Method Setter for validate size value"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = size
            self.height = size

    def __str__(self):
        """Method fot anulate __str__"""
        return("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))
