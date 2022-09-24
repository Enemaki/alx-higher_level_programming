#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    for c in dir():
        if c[:2] == "__":
            continue
        else:
            print("{}".format(c))
