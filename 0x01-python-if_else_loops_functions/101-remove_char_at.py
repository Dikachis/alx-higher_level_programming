#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str) or n < 0:
        return (str)
    copy = ""
    for i in range(len(str)):
        if i == n:
            copy = copy + ""
        else:
            copy = copy + str[i]
    return (copy)
