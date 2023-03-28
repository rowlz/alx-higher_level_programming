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
        """
        self.size = size

    @property
    def size(self):
        """ get size attr with property decorator
        Returns:
            int: the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Square class instance initialization
         Args:
             value (int): value of square.
         Raises:
             TypeError: value must be an integer
             ValueError: value must not be less than 0
         """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ The Area public instance method
        Return:
            int __area
        """
        self.__area = self.__size * self.__size
        return (self.__area)

    def my_print(self):
        """ Prints a square
        """
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
