#!/usr/bin/python3
""" Mylist module
"""


class MyList(list):
    """Mylist class that inherits from list class
    """

    def print_sorted(self):
        """returns a sorted list of assumed int type
        Args:
            self
        Return:
            sorted list
        """

        print(sorted(self))
