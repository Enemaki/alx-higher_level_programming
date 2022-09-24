#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv)
    if len(argv) == 0:
        print("{:d} arguments.".format(len(argv[0])))
    if len(argv) > 0:
        if len(argv) == 1:
            print("{:d} argument:".format(len(argv))
        else:
            print("{:d} arguments:".format(len(argv)))
        for i in range(1, num):
            print("{:d}: {:s}".format(i, argv[i]))


