# -*- coding: utf-8 -*-
"""
MIT 6.00.1x Introduction to Computer Science and Programming Using Python
Problem Set 1

Author: Ben Munns
"""

## Exercise 1
vowels = ['a', 'e', 'i', 'o', 'u']
s = 'azcbobobegghakl'
count = 0

for letter in s:
    if letter in vowels:
        count += 1

print('Number of vowels: ' + str(count))


## Exercise 2

substring = 'bob'
s = 'azcbobobegghakl'
count = 0
for i in range(len(s)):
    if s[i:i+len(substring)] == substring:
        count += 1

print('Number of times bob occurs is: ' + str(count))


## Exercise 3
s = 'azcbobobegghakl'
ss_curr = s[0]
ss_max = ss_curr

for i in range(1, len(s)):
    if ss_curr[-1] <= s[i]:
        ss_curr += s[i]
    elif len(ss_curr) > len(ss_max):
        ss_max = ss_curr
        ss_curr = s[i]
            
print('Longest substring in alphabetical order is: ' + str(ss_max))




""" Answers I liked
"""



s = 'azcbobobegghakl'

# Exercise 1 and 2 - one liners
print("Number of vowels:", sum(a in "aeiou" for a in s))

print("Number of times bob occurs is:", sum('bob' == s[i:i+3] for i in range(len(s))))

# Exercise 1-3 - recursive

def recur_sum(s):
    if not s:
        return 0
    else:
        return int(s[0] in 'aeiou') + recur_sum(s[1:])

print('Number of vowels:', recur_sum(s))


def recur_bob(s):
    if len(s) < 3:
        return 0
    else:
        return int(s[:3] == 'bob') + recur_bob(s[1:])

print('Number of times bob occurs is:', recur_bob(s))



def recur_lng(s, curr='', lngst=''):
    if not s:
        return curr if len(lngst) < len(curr) else lngst
    else:
        if not curr or s[0] >= curr[-1]:
            return recur_lng(s[1:], curr + s[0], lngst)
        else:
            if len(curr) > len(lngst):
                lngst = curr
            return recur_lng(s[1:], s[0], lngst)

print("Longest substring in alphabetical order is:", recur_lng(s))