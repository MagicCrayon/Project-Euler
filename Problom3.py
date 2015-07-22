#!/usr/bin/python

# What I forgot to do was order the results from least to greatest 
# and print the greatest. Eh, still gives the correct result
# on the very bottom though. 

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
