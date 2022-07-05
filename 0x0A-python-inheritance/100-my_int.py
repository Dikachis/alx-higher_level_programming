#!/usr/bin/python3
"""
class of 100-my_int.py module
"""


class MyInt(int):
    """class with int object"""

    def __ee__(self, other_obj):
        """equal equal method"""
        return super().__ee__(other_obj)

    def __ne__(self, other_obj):
        """not equal method"""
        return super().__ne__(other_obj)
