print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Variables
action1 = None
action2 = None
action3 = None
action4 = None

#Users first choice
action1 = input("\nYou awake to find yourself on a deserted island do you stay on the beach or explore the island? S or E: ").upper()

if action1 == "S": # You die
  print("\n You stay on the beach not exploring the island and eventually die from dehydration and starvation.\n\nTHE END")
else: # You go on
  action2 = input("\nYou decide to explore the island.\
                  \n While exploring you come across a cave, do you want to investigate the inside of the cave? Y or N: ").upper()
  if action2 =="N": # you die
    print("\nYou're too afraid to enter the cave, You go back to the beach not exploring the island any furher.\n\nTHE END")
  else: # You go on
    action3 = input("\nYou enter the cave and just a few steps into the cave, you notice a small mound of freshly dug soil.\
                      \nDo you want to start digging? Y or N: ").upper()
    if action3 =="N": # you die
      print("\nYou're too lazy to dig, you fall asleep on the ground.\n\nTHE END")
    else: # You go on
      action4 = input("\nYou dig down with your hands and find a small locked chest with 3 coloured keys.\
                      \nWhich key do you choose, Red, Yellow or Green? R,Y or G: ").upper()
      if action4 == "R" or action4 == "Y": # You die
        print("\nOh no, wrong key, it a trap!  The case explodes, blowing you to pieces!\n\nTHE END")
      else: # You WIN
        print("\nHooray!!! The chest opens and it's full of gold. \nYou Win. \nWell done!")
