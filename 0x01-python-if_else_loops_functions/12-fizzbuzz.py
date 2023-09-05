#!/usr/bin/python3
def fizzbuzz():
    for nez in range(1, 101):
        if nez % 3 == 0 and nez % 5 == 0:
            print("FizzBuzz", end=" ")
        elif nez % 3 == 0:
            print("Fizz", end=" ")
        elif nez % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(nez, end=" ")
