#!/usr/bin/python3

"""Programs that i am using to learn inheritance more in depth"""

class Rectangle(BaseGeometry):
    """A rectangle class inheriting from BaseGeometry"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
