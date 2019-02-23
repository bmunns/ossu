# Week 1 - Problem 1

s = input('Enter input: ')
vowel_counter = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')

print('Number of vowels: ' + str(vowel_counter))

#----------------------------------------------------------------------------------------
#Week 1 - Problem 2

s = input ('Enter input: ' )
bob_counter = 0
for index in range(len(s) - 2):
    if 'bob' in s[index:index+3]:
        bob_counter+=1
print('Number of times bob occurs is: ' + str(bob_counter))

#----------------------------------------------------------------------------------------
# Week 1 - Problem 3

s = input('Enter input: ' )
substring_output = ''
multi_substring = []

for index in range(len(s)-1):
    if s[index] > s[index + 1]:
        substring_output += s[index]
        multi_substring.append(substring_output)
        substring_output = ''
        next
    else:
        substring_output += s[index]

max = multi_substring[0]
    
if len(multi_substring) > 1:
   for index in range(len(multi_substring)):
    if len(max) < len(multi_substring[index]):
        max = multi_substring[index]

print('Longest substring in alphabetical order is:' + str(max))