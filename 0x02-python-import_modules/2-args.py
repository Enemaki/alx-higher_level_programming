#!/usr/bin/python3
if __name__ == "__main__":
    def no_of_args(*argv):
        if len(argv) == 0:
            print("{} arguments.".format(len(argv)))
        if len(argv) > 0:
            i = 1
            print("{} arguments.".format(len(argv)))
            for arg in argv:
                print("{}: {}".format(i, arg))
                i += 1
