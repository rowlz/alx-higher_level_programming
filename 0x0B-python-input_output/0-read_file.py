#!/usr/bin/python3
"""This is the read_file module
"""


def read_file(filename=""):
    """ read_file function reads a file and prints it to stdot
        Args:
            filename: file name variable
        Return:
            reads the file
    """

    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            print(line, end="")
