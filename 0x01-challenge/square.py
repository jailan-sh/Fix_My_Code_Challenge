#!/usr/bin/python3
""" class square"""


class Square():
    """ class square """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """constructor"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ get perimeter """
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        """ represent class object as string"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ object call """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
