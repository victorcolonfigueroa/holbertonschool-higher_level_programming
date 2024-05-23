#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, a special type of rectangle with equal sides.

    Attributes:
        size (int): The length of each side of the square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The length of each side of the square.
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Returns:
            str: A string in the format "[Square] size/size".
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
