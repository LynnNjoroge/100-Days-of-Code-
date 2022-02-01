import random

num = random.randint(1, 100)
#print(num)
guess = None

while guess != num:
    guess = int(input("guess a number between 1 and 100: "))
    
    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")