#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv) - 1
    if num == 0:
        print("{:d} arguments.".format(num))
    elif num == 1:
        print("{:d} argument:".format(num))
    else:
        print("{:d} arguments:".format(num))
    for a, s in enumerate(argv):
        print("{}: {}".format(a, s))


