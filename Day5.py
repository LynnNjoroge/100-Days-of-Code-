# Day5
# Random Password Generator Challenge
import random
import string

alphabet_string1 = string.ascii_lowercase
alphabet_string2 = string.ascii_uppercase
#Create a string of all lowercase and uppercase letters
alphabets = alphabet_string1 + alphabet_string2
letters = list(alphabets)
#Create a list of all lowercase letters
# print(letters)

numbers = [str(i) for i in range(0,10)]
#print(numbers)

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']
#print(symbols)
print("Welcome to the Python Password Generator!")
nr_letters = random.randint(3,7)
#int(input("How many letters would you like in your password? \n"))
nr_symbols = random.randint(3,7)
#int(input("How many symbols would you like in your password? \n"))
nr_numbers = random.randint(3,7) 
#int(input("How many numbers would you like in your password? \n"))

# Password generator
password_list = []

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

#print(password_list)
random.shuffle(password_list)
#print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your Password is {password}") 