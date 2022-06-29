#!/usr/bin/python3
class LockedClass:
    """A locked class that only allows the user to dynamically
    create the instance attribute 'first_name'
    """
    __slots__ = ['first_name']
