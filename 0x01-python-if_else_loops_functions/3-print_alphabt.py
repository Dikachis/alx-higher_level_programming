#!/usr/bin/python3

for index in range(97, 123):
    if (chr(index) != 'e' and chr(index) != 'q'):
        print("{:c}".format(index), end='')
