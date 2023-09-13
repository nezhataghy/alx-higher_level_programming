#!/usr/bin/python3
def uniq_add(my_list=[]):
    somme = 0
    for num in set(my_list):
        somme += num
    return (somme)
