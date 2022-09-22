#!/usr/bin/python3
for i in range(8):
    for j in range(1, 10):
        if ((i == j) or (i > j)):
            continue
        else:
            print("{}{}, ".format(i, j), end="")
print("89")
