#!/usr/bin/python3
'''Defines a text-indentation function'''


def text_indentation(text):
    '''Print text with two new lines after each '.', '?', and ':'.
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    var = 0
    while var < len(text) and text[var] == ' ':
        var += 1

    while var < len(text):
        print(text[var], end="")
        if text[var] == "\n" or text[var] in ".?:":
            if text[var] in ".?:":
                print("\n")
            var += 1
            while var < len(text) and text[var] == ' ':
                var += 1
            continue
        var += 1
