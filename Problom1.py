#!/usr/bin/python

numbers = range(1, 1000)
count = 0
for i in numbers:
    if isMul(i) == True:
        count = count + i

print "Sum: ", count

def isMul (i):
    return (i % 3 ==0) or (i % 5 == 0)
