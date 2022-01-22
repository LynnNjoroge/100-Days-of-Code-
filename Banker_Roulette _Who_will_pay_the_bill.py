# Banker Roulette - Who will pay the bill

import random

bankers_names = input("Give the names of everybody dining, separated by a comma. ")
names = bankers_names.split(", ")

# print(names)

banker_paying = random.choice(names)

print(banker_paying + " is going to pay for everyone's meal")
