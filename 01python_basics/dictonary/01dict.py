# dictonary : A dictionary is a collection of key-value pairs in Python.
#  Each key is unique and is used to store and retrieve values.

# dictionaries are defined using curly braces {}
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}


# how to access values/ individual item in dictionary 

# my_dict['key'] # it will return value associated with the key and if key is not found it 
# will raise KeyError

name = my_dict['name']  # accessing value using key 'name'
print("Name:", name)  # Output: Name: Alice

# to avoid KeyError we can use get() method, It will return None if key is not found instead of raising error


age = my_dict.get('age1')  # accessing value using get() method
print("Age:", age)  # Output: Age: None



# when we iterate over dictionary it will give keys by default 
# later by using key we can access value 

for key in my_dict:
    print(key, ":", my_dict.get(key))  # accessing value using key

# we can use two variables in for loop to get key and value both using items() method

for key,value in my_dict.items():
    print(key, "->", value)   
# .items() method returns a view object that displays a list of a dictionary's key-value tuple pairs.


# add a new key-value pair to the dictionary
my_dict['profession'] = 'Engineer'
print(my_dict)

# as dictinary has no order we cannot use insert method like list to add key-value pair at specific position and also pop(key) takes key as argument to remove key-value pair
removed_value = my_dict.pop('city')  # removes the key 'city' and returns
print("Removed Value:", removed_value)  # Output: Removed Value: New York

# del keyword can also be used to remove key-value pair
del my_dict['age']  # removes the key 'age'
print(my_dict)

# methods of dictionary
# 1. keys() - returns a view object containing all the keys in the dictionary
keys = my_dict.keys()
print("Keys:", keys)
# 2. values() - returns a view object containing all the values in the dictionary
values = my_dict.values()

# 3. update() - updates the dictionary with key-value pairs from another dictionary or iterable of key-value pairs
new_data = {'country': 'USA', 'occupation': 'Software Developer'}
my_dict.update(new_data)
print("Updated Dictionary:", my_dict)

# 4. clear() - removes all key-value pairs from the dictionary
# my_dict.clear()

# 5. copy() - returns a shallow copy of the dictionary
# my_dict_copy = my_dict.copy()

# 6. fromkeys() - creates a new dictionary with keys from an iterable and values set to a specified value
keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)  # creates a dictionary with keys 'a', 'b', 'c' and all values set to 0 

print("New Dictionary from keys:", new_dict)
# 7. setdefault() - returns the value of a key if it is in the dictionary; if not, it inserts the key with a specified value
value = my_dict.setdefault('hobby', 'Reading')  # adds key 'hobby with value 'Reading' if not present
print("Value of 'hobby':", value)
print("Dictionary after setdefault:", my_dict)  



# nested dictionary : A nested dictionary is a dictionary that contains another dictionary as a value for one of its keys.
nested_dict = {
    'person1': {
        'name': 'John',
        'age': 25
    },
    'person2': {
        'name': 'Jane',
        'age': 28
    }
}

# accessing values in nested dictionary

print(nested_dict['person2'])  #{'name': 'Jane', 'age': 28}


# lets see dictionary comprehension : It is a concise way to create dictionaries using a single line of code.

squares = {
         x:x*x for x in range(1,9)
}
# x : is key and x*x is value for that key

print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}



# key set 
my_keys = ['name', 'age', 'city']
 
my_valuse=['Bob', 35, 'Los Angeles']

# above two list which are iterable can be used to create dictionary using zip() function

zipped_dict= {k:v for k,v in zip(my_keys,my_valuse)}
