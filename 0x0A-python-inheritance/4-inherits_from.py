#!/usr/bin/python3
"""inherits from module
"""


def inherits_from(obj, a_class):
    """ checks if an object inherits from a subclass
    Args:
        obj: object variable
        a_class: specified class
    Return:
        True or False
    """

    obj_type = type(obj)
    if (obj_type != a_class):
        return issubclass(type(obj), a_class)
    else:
        return False
