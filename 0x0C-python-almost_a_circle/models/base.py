#!/usr/bin/python3
"""This is the base class module"""


class Base:

    """Base Class
    Attributes:
        id(int)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """This is the class constructor, called when object is made
        Args:
            id: int variable
        Returns
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
