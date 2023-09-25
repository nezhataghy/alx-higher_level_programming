#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_elem = 0

    try:
        for index in range(x):
            print("{}".format(my_list[index]), end="")
            num_elem += 1
    except:
        pass
    print()
    return num_elem
