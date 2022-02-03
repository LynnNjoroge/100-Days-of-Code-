'''Write a function named online_count that takes one parameter. 
The parameter is a dictionary that maps from strings of names to the string "online" or "offline"
Your function should return the number of people who are online.'''

# long version
from itertools import count

people = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    "Ev2": "online",
}

def online_count(people):
    count = 0
    for person, status in people.items():
        if status == "online":
            count += 1
    return count
print(online_count(people))


# short version
def online_count(people):
    return len([p for p in people if people[p] == "online"])
print(online_count(people))
