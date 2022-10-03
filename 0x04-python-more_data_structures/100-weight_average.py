#!/usr/bin/python3
def weight_average(my_list=[]):
    a = 0
    b = 0
    result = 0
    for item in my_list:
        a += item[0] * item[1]
        b += item[1]
    result = a / b
    return result
