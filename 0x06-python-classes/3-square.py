#!/usr/bin/python3

""" A square class
"""


class Square:
    """ An square class that defines a square with size
    """

    def __init__(self, size=0):
        """ The Square class initialization
        Args:
            size: size of the square, defalts to 0
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ The Area public instance method
        Return:
            int __area
        """

        self.__area = self.__size * self.__size
        return (self.__area)
