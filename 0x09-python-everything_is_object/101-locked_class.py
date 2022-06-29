#!/usr/bin/python3
class LockedClass:
    """
    A locked class that only allow the user from dynamically
    create the instance attribute 'first_name'
    """
    __slots__ = ['first_name']
