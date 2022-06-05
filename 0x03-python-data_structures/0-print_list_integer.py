#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for index in range(len(my_list)):
        print("{}".format("\n".join(my_list[index])))
