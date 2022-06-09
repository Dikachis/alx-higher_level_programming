#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    suma = 0
    prom = 0
    for i in my_list:
        suma += i[0] * i[1]
        prom += i[1]
    return suma/prom
