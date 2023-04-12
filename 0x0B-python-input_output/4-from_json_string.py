#!/usr/bin/python3
"""This is the from_json_string module
"""


import json


def from_json_string(my_str):
    """ from_json_string returns an object rep by a JSON string
        Args:
            my_str: string variable
        Return:
            an object rep by a JSON string
    """

    return (json.loads(my_str))
