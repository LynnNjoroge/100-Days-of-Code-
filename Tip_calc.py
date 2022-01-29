#Tip Calculator

print('Welcome to the Tip Calculator')
bill = float(input('What was your total bill?  $'))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input('How many people are splitting the bill? '))
tip_percent = tip/100
total_tip = bill * tip_percent
pay = bill + total_tip
split_pay = pay / people
final_bill = round(split_pay, 2)
final_bill = "{:.2f}".format(split_pay)
print(f'Each person should pay ${final_bill}')