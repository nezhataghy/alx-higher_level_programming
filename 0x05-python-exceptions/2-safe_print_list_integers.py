#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_elem = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            num_elem += 1
        except Exception:
            pass

    print()
    return (num_elem)
