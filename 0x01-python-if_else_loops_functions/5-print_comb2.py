#!/usr/bin/python3
for i in range(0, 100):
    print("{:0>2d}".format(i), sep=',', end=', ')
print("{:0>2d}".format(99))
