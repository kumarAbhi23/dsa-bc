import random



# print(random.randrange(1,10)) # prints a random integer from 1 to 9

# random inteeger from 1 to 10

print(random.randint(1,10)) # last number is inclusive


list_items=['apple','banana','mango','grapes']

print(random.choice(list_items))  # prints a random item from the list

print(random.choices(list_items,k=3))  # prints k random items from the list with replacement


print(random.shuffle(list_items))  # shuffles the original list

