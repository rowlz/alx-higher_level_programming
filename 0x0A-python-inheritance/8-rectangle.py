#!/usr/bin/python3
""" Rectangle Module
Attributes:
    BaseGeometry (object): Base Geometry class
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):

    """ Rectangle Class
    """

    def __init__(self, width, height):
        """ Initialization
        Args:
            width (int): the width
            height (int): the height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
