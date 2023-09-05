#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = abs(number) % 10
if number < 0:
    l_digit = - l_digit
if l_digit > 5:
    print('Last digit of {} is {} and is greater than 5'.format(number, l_digit))
elif l_digit == 0:
    print('Last digit of {} is {} and is 0'.format(number, l_digit))
else:
    print('Last digit of {} is {} and is less than 6 and not 0'.format(number, l_digit))
