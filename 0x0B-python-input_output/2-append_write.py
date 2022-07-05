#!/usr/bin/python3
"""The append text function container"""


def append_write(filename="", text=""):
    """appends a string and returns the number of characters added"""
    with open(filename, "a", encoding="utf-8") as file:
        lines = file.write(text)
        return lines
