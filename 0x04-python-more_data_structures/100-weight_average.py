#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    num = 0
    denom = 0
    for tuple_ in my_list:
        num += (tuple_[0] * tuple_[1])
        denom += tuple_[-1]
    return (num/denom)
