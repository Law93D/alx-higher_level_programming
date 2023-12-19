#!/usr/bin/python3
"""Defines a Square class with a private instance attribute."""

class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initializes the Square instance."""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
