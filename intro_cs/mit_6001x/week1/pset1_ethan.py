# Problem 1
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

s = 'azcbobobegghakl'

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0

for char in s:
    if char in vowels:
        vowel_count = vowel_count + 1

print('Number of vowels: ' + str(vowel_count))


# Problem 2
# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

s = 'azcbobooboegbobghaklbobob'

times = 0

for i in range(len(s)):
    try:
        if s[i] == 'b':
            if s[i+1] == 'o':
                if s[i+2] == 'b':
                        times = times + 1
    except(IndexError):
        # end of s met
        continue

print("Number of times bob occurs is: " + str(times))


# Problem 3
# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. 
# For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

s = 'wenjcxnuihwmciqjwsyducabcde'

temp = ''
substring = ''

for i in range(len(s)):
    try:
        temp = temp + s[i]
        if s[i] <= s[i + 1]:
            if len(temp) > len(substring):
                substring = temp
        else:
            if s[i] >= s[i-1] and len(temp) > len(substring):
                substring = temp
            temp = ''
    except(IndexError):
        # end of s met
        if len(temp) > len(substring):
            substring = temp
        continue

print("Longest substring in alphabetical order is: " + substring)