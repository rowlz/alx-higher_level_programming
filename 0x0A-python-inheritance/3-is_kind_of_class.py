#!/usr/bin/python3
"""is_of_kind_class module
"""


def is_kind_of_class(obj, a_class):
    """ checks wether an instance is of a specified class
        (or inherited from another class that inherits)
    Args:
        obj: object variable
        a_class: specified class
    Return:
        True or False
    """

    return (isinstance(obj, a_class))
