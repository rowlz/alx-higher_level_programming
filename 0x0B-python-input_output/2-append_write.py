#!/usr/bin/python3
"""This is the append_write module
"""


def append_write(filename="", text=""):
    """ append_write function appends a string at end of file
        Args:
            filename: file name variable
            text:     str inpt variable
        Return:
            number of char added
    """

    with open(filename, mode='a', encoding='utf-8') as a_file:
        a_file.write(text)

    return len(text)
