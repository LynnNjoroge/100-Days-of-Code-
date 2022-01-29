# The Hangman Challenge
'''The main goal here is to create a sort of “guess the word” game. The 
user needs to be able to input letter guesses. '''
import random
from hangman_art import stages, logo
from hangman_words import word_list

# Welcoming the user
username = input("What is your name? ")
print("Hello " + username + " Welcome to the \n" + logo)

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6
lives = 6

# create an empty list called display and populate it with blanks equal to the word length
display = []
for i in range(word_length):
    display += "_"
print(f"The chosen word has {word_length} letter")
print(display)


while not end_of_game:
    # ask the user to guess any letter
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
      print(f"You guessed {guess}, which is not in the word. You lose a life")
      lives -=1
      if lives == 0:
          end_of_game = True
          print("You lose. ")
     #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win")

    #print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

