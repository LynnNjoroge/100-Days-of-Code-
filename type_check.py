''' Write a function named only_ints that takes two parameters. 
Your function should return True if both parameters are integers, and False otherwise.'''

def only_ints(a, b):
    return type(a) == int and  type(b) == int

print(only_ints(1, 2))
print(only_ints('a', 2)