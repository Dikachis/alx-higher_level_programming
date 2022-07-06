#!/usr/bin/python3
"""
9-student Module
"""


class Student:
    """
    Student class
    """


def __init__(self, first_name, last_name, age) -> None:
    """
    initialization special method
        Args:
            first_name: first name of student
            last_name: last name of student
            age: age of student
    """
    self.first_name = first_name
    self.last_name = last_name
    self.age = age


def to_json(self, attrs=None):
    """
    Retrieves dictionary representation of Student
        Args:
            attrs: initial list
            Returns: a dictionary representation of a Student
    """
    if attrs is None or not all([type(attr) is str for attr in attrs]):
        return self.__dict__.copy()

    dic_repr = dict()
    for key, value in self.__dict__.items():
        if key in attrs:
            dic_repr[key] = value

    return dic_repr
