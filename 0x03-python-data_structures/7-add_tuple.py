#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    size1 = len(tuple_a) - 1
    size2 = len(tuple_b) - 1
    res = []
    if size1 == 1:
        tuple_a = (tuple_a[0], 0)
    elif size2 == 1:
        tuple_b = (tuple_b[0], 0)
    elif size1 == 0:
        tuple_a = (0, 0)
    elif size2 == 0:
        tuple_b = (0, 0)
    for i in range(0, 2):
        res = res.append(tuple_a[i] + tuple_b[i])
    res = tuple(res)
    return res
