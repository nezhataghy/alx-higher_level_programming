#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx <= (len(my_list) - 1):
        new_list = my_list.copy()
        new_list[idx] = element
    return (new_list)
