#!/usr/bin/python3
"""This is the write_file module
"""


def write_file(filename="", text=""):
    """ write_file function write a file and prints it to stdot
        Args:
            filename: file name variable
            text:     characters to write into file
        Return:
            reads the file
    """

    n_char = 0

    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(text)

    for c in text:
        n_char += 1

    return (n_char)
