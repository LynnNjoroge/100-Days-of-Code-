#use Dictionary Comprehension to create a dictionary called result 
# that takes each word in the given sentence and calculates the number of letters in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

split_sentence = sentence.split(" ")

result = {word:len(word) for word in split_sentence}

print(result)