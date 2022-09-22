#!/usr/bin/python3
def islower(c):
    for a in range(ord('a'), ord('z')+1):
        if c == chr(a):
            return True
    else:
        return False
