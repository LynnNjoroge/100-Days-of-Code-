# Anagram - word, phrase, or name formed by rearranging the letters of another,
# write a program that checks if two words are anagrams

from collections import Counter

# solution1 using Counter 
def check_anagram(x, y):
    ''' function to check if two strings are anagram or not'''
    if(Counter(x) == Counter(y)):
        print("The strings are anagrams.")
    else:
        print("The strings are NOT anagrams.")
 
 
# check if it works
x = "listen"
y = "silent"
check_anagram(x, y)

# solution2 using the sorted function
def is_anagram(a, b):
    ''' function to check if two strings are anagram or not'''
    # the sorted strings are checked
    if(sorted(a)== sorted(b)):
        print("The strings are anagrams.")
    else:
        print("The strings are NOT anagrams.")        
         
# checking if it works 
a ="cute"
b ="boot"
is_anagram(a,b)