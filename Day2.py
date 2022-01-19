#write a program using maths and f-Strings that tells us how many years, months, weeks and days we habe left if we live to be 100 years old

age = input('How old are you now?')
age_int = int(age)
years_left = 100 - age_int
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

message = f"You have {years_left} years, {months_left} months, {weeks_left} weeks and {days_left} days left to live"

print(message)