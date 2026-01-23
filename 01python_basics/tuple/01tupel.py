# tuple :
# A tuple is an ordered, immutable collection of elements in Python.
# Tuples are defined using parentheses ().

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements in a tuple
print("First element:", my_tuple[0])  # Output: First element: 1
print("Last element:", my_tuple[-1])  # Output: Last element: 5

# Slicing a tuple
print("Slice from index 1 to 3:", my_tuple[1:4])  # Output: Slice from index 1 to 3: (2, 3, 4)

# Tuples are immutable, so we cannot modify them directly
# However, we can create a new tuple by concatenating existing tuples
new_tuple = my_tuple + (6, 7)
print("New tuple:", new_tuple)  # Output: New tuple: (1, 2, 3, 4, 5, 6, 7)

# Counting occurrences of an element in a tuple
count = my_tuple.count(2)
print("Count of '2':", count)   # Output: Count of '2': 1

# Finding the index of an element in a tuple
index = my_tuple.index(4)
print("Index of '4':", index)   # Output: Index of '4': 3

# Converting a list to a tuple
my_list = [10, "hello", True]
converted_tuple = tuple(my_list)
print("Converted Tuple:", converted_tuple)   # Output: Converted Tuple: (10, 'hello', True)

# Using tuples as keys in dictionaries (since they are immutable)
tuple_dict = {(1, "a"): "value1", (2, "b"): "value2"}
print("Dictionary with tuples as keys:", tuple_dict)


# unrap tuple 
t1=(1,2,3)
(a,b,c)=t1
print(a)