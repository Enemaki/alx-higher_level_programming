#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for k in set(my_list):
        result += k
    return result
