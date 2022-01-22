# Rollecoaster Ticketing Challenge
print("Welcome to the Rollercoaster Ride")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can reide the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 7
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a phot taken? Y or N.").upper()
    if wants_photo == "Y":
        #add $3 to bill
        bill += 3
        print(f"Your final bill is ${bill}")
else:
    print("Sorry, you are not tall enough to ride this rollercoaster")


    
