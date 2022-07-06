#!/usr/bin/python3
"""
"Student class" cotainer
"""


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__.copy()

    new_dict = dict()
    for key, value in self.__dict__.items():
        if key in attrs:
            new_dict[key] = value

    return new_dict
