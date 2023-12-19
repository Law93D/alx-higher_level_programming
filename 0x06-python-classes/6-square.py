#!/usr/bin/python3
"""Defines a Square class with size and position attributes."""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the Square instance."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position attribute"""
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(i, int) for i in value) \
                or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' character and position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
