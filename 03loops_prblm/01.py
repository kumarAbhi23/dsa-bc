'''
given a list of numbers calculate count of postive numbers in the list


'''

numbers = [-10, -5, 3, -1, 0, 7, -2]
count_positive = 0

for num in numbers:
    if num>0:
        count_positive += 1

print("Count of positive numbers:", count_positive)
