#!/usr/bin/python3
def uppercase(str):
    for lettre in str:
        if ord(lettre) > 96 and ord(lettre) < 123:
            lettre = chr(ord(lettre) - 32)
        print("{:s}".format(lettre), end='')
    print()
