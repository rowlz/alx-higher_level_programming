#!/usr/bin/python3
"""This is the to_json_string module
"""


import json


def to_json_string(my_obj):
    """ to_json_string returns the json rep of an object
        Args:
            my_obj: object variable
        Return:
            the JSON of the object
    """

    return (json.dumps(my_obj))
