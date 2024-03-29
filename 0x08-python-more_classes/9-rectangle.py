#!/usr/bin/python3
""" Rectangle module
"""


class Rectangle:

    """ Rectangle Class object
    Attributes:
        height (int): height value
        width (int): width value
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width getter function
        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, width_val):
        """ width setter function
        Args:
            width_val (int): The width value
        Raises:
            TypeError: Width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(width_val, int):
            raise TypeError("width must be an integer")
        if width_val < 0:
            raise ValueError("width must be >= 0")
        self.__width = width_val

    @property
    def height(self):
        """ height getter
        Returns:
            int: height
        """
        return self.__height

    @height.setter
    def height(self, height_val):
        """height setter function
        Args:
            height_val (int): Description
        Raises:
            TypeError: height must an integer
            ValueError: height must >= 0
        """
        if not isinstance(height_val, int):
            raise TypeError("height must be an integer")
        if height_val < 0:
            raise ValueError("height must be >= 0")
        self.__height = height_val

    def area(self):
        """Area function to calculate the area of the rectangle
        Returns: an iint value of the area
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """Perimeter funtion to calculate perimeter of the rectangle
        Returns: an int value of preimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """ __str__ prints rectangles
        Returns:
            str:  # rectangles
        """
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        else:
            i = 0
            while i < self.__height:
                string += (str(self.print_symbol) * self.__width)
                if i != self.__height - 1:
                    string += "\n"
                i += 1
            return string

    def __repr__(self):
        """__repr__ recreats an instance
        Returns: a string
        """
        return f"Rectangle({self.__width:d}, {self.__height:d})"

    def __del__(self):
        """__del__ deletes an instance of the object
        Returns: a string bye rectangle...
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_smaller that returns the biggest rectammgle based on area
        Returns: a the instance rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
