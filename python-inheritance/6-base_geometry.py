#!/usr/bin/python3
class BaseGeometry:
    """
    This is the base class for geometry objects.
    """

    def area(self):
        """
        Calculates the area of the geometry object.
        This method should be implemented by subclasses.
        """
        raise Exception("area() is not implemented")
