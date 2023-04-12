#!/usr/bin/python3
"""This is the save_to_json_file module
"""


import json


def save_to_json_file(my_obj, filename):
    """ save_to_json_file function write an Object to a text file
        Args:
            filename: file name variable
            my_obj:   object file
        Return:
            reads the file
    """

    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(json.dumps(my_obj))
