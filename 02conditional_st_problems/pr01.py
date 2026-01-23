# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

# we take input from the user

age = int(input("enter your age:"))

# input() is a function that takes input from the user as a string.
# int() is a function that converts a string to an integer.

# if age <13 : child
if age < 13:
    print("Child")
# if age >=13 and age <=19 : teenager
elif age >= 13 and age <= 19:   
    print("Teenager")
# if age >=20 and age <=59 : adult
elif age >= 20 and age <= 59:
    print("Adult")
# if age >=60 : senior
else:
    print("Senior")

