#!/usr/bin/python3
"""This is the load_from_json_file module
"""


import json


def load_from_json_file(filename):
    """ load_from_json_file function create an Object from a text file
        Args:
            filename: file name variable
        Return:
            an object
    """

    with open(filename, encoding='utf-8') as a_file:
        return (json.load(a_file))
