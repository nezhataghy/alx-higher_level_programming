#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_of_keys = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            list_of_keys.append(i)
    j = 0
    while j < len(list_of_keys):
        del a_dictionary[list_of_keys[j]]
        j += 1
    return a_dictionary
