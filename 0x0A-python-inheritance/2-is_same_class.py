#!/usr/bin/python3
"""is same class module
"""


def is_same_class(obj, a_class):
    """ checks wether an object is an instance of a class
    Args:
        obj: object variable
        a_class: specified class
    Return:
        True or False
    """

    return type(obj) == a_class
