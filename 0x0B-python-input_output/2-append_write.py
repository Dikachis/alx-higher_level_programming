#!/usr/bin/python3
"""The read_file function container"""


def append_write(filename="", text=""):
    """""reads a text file(UTF8) and prints it to stdout"""
    with open(filename, "a", encoding="utf-8") as file:
        lines = file.read()
        for line in lines:
            text.append(str(line))
        return (text)
