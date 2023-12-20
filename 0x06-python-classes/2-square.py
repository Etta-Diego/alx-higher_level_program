#!/usr/bin/python3
"""
    This module defines a class
"""


class Square:
    """
    A class Square that defines a square
    Attributes:
    __size(int): The square's size

    """

    def __init__(self, size):
        
        # Initializes a new instance of square.
        # Args:
        # size(int): The size of the square
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size
