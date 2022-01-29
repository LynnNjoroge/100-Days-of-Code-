# Caesar Cipher code Challenge
import random
import string
from caesar_cipher_art import logo

alphabet_string = string.ascii_lowercase
alphabet_string1 = string.ascii_lowercase
letters = alphabet_string + alphabet_string1
alphabet = list(letters)

print(logo)

def caesar(beg_text, no_of_shifts, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
            no_of_shifts *=-1

    for i in beg_text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + no_of_shifts
            end_text += alphabet[new_position]
        else:
            end_text += i
            
    print(f"The {cipher_direction} text of your message is {end_text}")  
    
    
should_end = False

while not should_end:
    direction = input("Type 'encode' to encryt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number: \n"))
    shift = shift % 26

    caesar(beg_text=text, no_of_shifts=shift, cipher_direction=direction)

    go_on = input("Type 'yes' if you want to go on or 'no' to end the program \n").lower()

    if go_on == "no":
        should_end = True
        print("Goodbye")



