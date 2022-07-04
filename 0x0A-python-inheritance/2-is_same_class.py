#!/usr/bin/python3
"""
This is a module container of the function 2-is_same_class
"""


def is_same_class(obj, a_class):
    """
    To check if the object is exactly an instance of the specified class
        Args:
            obj: initial object
            a_class: class to confirm with the object
            Returns: True if object is an exactly the instance of the class
                     or False if not
    """
    if type(obj) is not a_class:
        return False
    else:
        return True
