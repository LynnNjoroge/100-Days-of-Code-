''' Suppose you are prompted to write a Python program that interacts with a user in a console window. 
You may be accepting input to send to a database, or reading numbers to use in a calculation.
write a simple program to achieve this'''

while True:
    reply = input("Enter Text: ")
    if reply == 'stop': break
    print(reply)