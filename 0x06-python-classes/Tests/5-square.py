#!/usr/bin/python3
""" Square module """


class Square:
    """ Declares a square class """

    def __init__(self, size=0) -> None:
        """
        Intializes the attributes

        Args:
            size: size of square
        """
        self.size = size

    @property
    def size(self):
        """ Gets the attribute to be used in class """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Computes area of a square """
        return self.__size ** 2

    def my_print(self):
        """ Prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            integer = 0
            while integer < self.__size:
                number = 0
                while number < self.__size:
                    print("{}".format("#"), end='')
                    number += 1
                print()
                integer += 1
