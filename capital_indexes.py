'''Write a function named capital_indexes. 
The function takes a single parameter, which is a string. 
Your function should return a list of all the indexes 
in the string that have capital letters.'''

def capital_indexes(s):
    return [idx for idx, letter in enumerate(s) if letter.isupper()]

print(capital_indexes("HelLO"))

def capital_indexes(word):
    letters = []
    for i in enumerate(word):
       if i[1].isupper():         
           letters.append(i[0])
    return letters

word = "HelLO"
output_list =  capital_indexes(word)
print(output_list)