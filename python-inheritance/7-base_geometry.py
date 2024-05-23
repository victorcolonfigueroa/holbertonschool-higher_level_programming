#!/usr/bin/python3
class BaseGeometry:
    """
    A base class for geometry operations.
    """

    def area(self):
        """
        Calculates the area of the geometry.
        Raises:
            Exception: If the method is not implemented in the subclass.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if a value is an integer and greater than 0.
        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
