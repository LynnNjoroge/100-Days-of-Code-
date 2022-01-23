# create a program that calculates students average height
# use for loops

students_heights = input("Enter a list of student heights separated by a space: ").split()
for i in range(0, len(students_heights)):
    students_heights[i] = int(students_heights[i])
    # print(students_heights)

total_height = 0
for h in students_heights:
    total_height += h 
print(f"The total height of all students is {total_height}")

number_of_students = 0
for s in students_heights:
    number_of_students += 1
print(f"The number of students in the class is {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"The average height os students is {average_height}")