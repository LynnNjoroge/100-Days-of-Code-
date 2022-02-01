'''Write a function named mid that takes a string as its parameter. 
Your function should extract and return the middle letter. 
If there is no middle letter, your function should return the empty string.'''

def mid(s):
    if len(s) % 2 == 0:
        return "no middle letter"
    return s[len(s)//2]

print(mid("abc"))
print(mid("aaaa"))