# Virtual coin toss

import random
random_side = random.randint(0, 1)

if random_side ==1:
    print("Heads")
else:
    print("Tails")

# we can also use random.choice
another_way = random.choice(["Heads", "Tails"])
if another_way == "Heads":
    print("Heads")
else:
    print("Tails")
