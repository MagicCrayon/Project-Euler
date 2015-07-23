#!/usr/bin/python

def isPalindrome(x):
    return str(x) == str(x)[::-1]

Numbers = list(range(100, 999))
Palindromes = []

for x in Numbers:
    for y in Numbers:
        if (isPalindrome(x*y)):
            i = x*y
            Palindromes.append([i])
        continue

print max(Palindromes)

