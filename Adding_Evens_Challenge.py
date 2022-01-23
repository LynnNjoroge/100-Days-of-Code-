# write a program that calculates the sum 
# of all even numbers between 1 to 100
# including 1 and 100
# these should only be one statement printed to the console

total = 0

for i in range(1, 101):
    if i % 2 == 0:
        total += i
print(f"The total of all even numbers between 1 to 100 is: {total}")