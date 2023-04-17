#!/usr/bin/python3
""" Rectangle Module
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class
    Attribtes:
        width: width int variable
        Height: height int variabel
        x: variable
        y: variable
    """

    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """init funtion
        ARGS
            width: width vriable
            height: height variable
            x= int varaibale
            y= int variable
            id= int variable
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        Base.__init__(self, id)

    @property
    def width(self):
        """ width getter
        Returns:
                int: the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter
        Args:
                value (int): width value
        Raises:
                TypeError: width must be an integer
                ValueError: must be > 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter
        Returns:
                int: the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        Args:
                value (int): height value
        Raises:
                TypeError: height must be an integer
                ValueError: must be > 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter
        Returns:
                int: x value
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter
        Args:
                value (int): x value
        Raises:
                TypeError: x must be an integer
                ValueError: x must be >= 0
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter
        Returns:
                int: y value
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y setter
        Args:
                value (int): y value
        Raises:
                TypeError: y must be an integer
                ValueError: y must be >= 0
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
