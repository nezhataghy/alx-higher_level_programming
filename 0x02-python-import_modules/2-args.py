#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    i = 1

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(count))
        for arg in argv:
            if arg != argv[1]:
                print("{}: {}".format(i, arg))
                i += 1
