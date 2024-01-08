#!/usr/bin/python
"""
class:
    A class that inherits from list
"""


class MyList(list):
    """
    module:
        public instance method that prints the list,
        but sorted (ascending sort)
    """
    def print_sorted(self):
        """
        args:
            elements to be sorted
        """
        print(sorted(self))
