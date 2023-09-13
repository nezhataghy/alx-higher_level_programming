#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)
    output = 0
    size = len(roman_string)

    D = {"I": 1, "V": 5, "X": 10,
         "L": 50, "C": 100, "D": 500, "M": 1000}

    for i in range(size):
        if D.get(roman_string[i], 0) == 0:
            return (0)

        if (i < (size - 1) and D[roman_string[i]] < D[roman_string[i + 1]]):
            output -= D[roman_string[i]]
        else:
            output += D[roman_string[i]]
    return (output)
