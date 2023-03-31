#!/usr/bin/python3
""" text_indentation module
    prints a text with 2 new lines after certain characters
    """


def text_indentation(text):
    """Prints text with 2 new lines after characters
    Arguments:
        text (string) : Text passage
    Raises:
        TypeError: text must be a string
    Returns:
        string: Text seperated with new lines
    """

    HasPrint = False

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for chars in text:
        if chars == "." or chars == "?" or chars == ":":
            print("{}\n\n".format(chars), end="")
            HasPrint = True
        elif HasPrint is True and chars == " ":
            print("{}".format(""), end="")
            HasPrint = False
        else:
            print("{}".format(chars), end="")
