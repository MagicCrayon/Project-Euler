#!/usr/bin/python

number = 600851475143
i = 2

while not(i > number):
    answer = number % i
    if answer == 0:
        print i
        number = number / i
        i = i + 1
        continue
    elif answer != 0:
        i = i + 1
        continue
