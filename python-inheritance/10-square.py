#!/usr/bin/python3
"""Square #1"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of a square"""

    def __init__(self, size):
        """
        Instantiation of the Square class.

        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): The size of the square.

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
