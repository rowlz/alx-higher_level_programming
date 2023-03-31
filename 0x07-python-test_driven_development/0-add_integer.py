#!/usr/bin/python3
""" add_integer module
    adds 2 numbers and retunrs result
    """


def add_integer(a, b=98):
    """Adds 2 numbers a float or integet
    Arguments:
        a (int, float): first arguement
        b (int, float, optional): default value 98
    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer
    Returns:
        int value of the sum of a + b
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
