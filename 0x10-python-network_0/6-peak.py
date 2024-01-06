#!/usr/bin/python3
"""Find a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """
    Finds the peak in a list of numbers
    """
    max_peak = None
    for i in range (1,len(list_of_integers) - 1):
        if list_of_integers[i] >= list_of_integers[i-1] and list_of_integers[i] >= list_of_integers[i+1]:
            if max_peak:
                max_peak = max(max_peak,list_of_integers[i])
            else:
                max_peak = list_of_integers[i]
                
    return max_peak
