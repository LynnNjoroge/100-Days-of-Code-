# write a program that censors cuss words in a sentence


from better_profanity import profanity

text = input("Please input the text you would like to censor: ")

def remove_cuss_words(text):
    censored = profanity.censor(text)
    return censored
    

#text = "Please leave me alone and just piss off"

print(remove_cuss_words(text))
