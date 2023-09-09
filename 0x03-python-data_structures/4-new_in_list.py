#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if idx >= 0 and idx <= (len(my_list) - 1):
        copy[idx] = element
    return (copy)
