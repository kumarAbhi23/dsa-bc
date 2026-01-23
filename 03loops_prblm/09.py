''''
check if all element are unique in list if duplicate found exit loop and print duplicate 


'''

lst=['banana','oranges','apple','mango']

# we will use set

unique_items=set()

for item in lst :
    if item in unique_items:
        print('duplicate item is :',item)
        break
    # before adding item to set check if it is already present
    
    unique_items.add(item)


    
