#!/usr/bin/python3
"""Lookup module
"""


def lookup(obj):
    """ returns the list of all methods in the object
    Args:
        obj: object variable
    Return:
        List of methods in the object
    """

    return (dir(obj))
