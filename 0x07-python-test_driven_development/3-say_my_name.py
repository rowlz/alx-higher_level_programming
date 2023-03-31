#!/usr/bin/python3
""" say_my_name module
    prints first name and last name
    """


def say_my_name(first_name, last_name=""):
    """Prints the first name and last name variables
    Arguments:
        first_name (string): first arguement
        last_name (string, optional): default value is empty, 2nd arguement
    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    Returns:
        string: My name is <first_name> <last_name>
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
