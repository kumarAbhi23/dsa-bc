# methods of lists

my_list = [10, 20, 30, 40, 50]

# 1. append() - adds an element to the end of the list
my_list.append(60)

# 2. insert() - inserts an element at a specified position
my_list.insert(2, 25)  # insert 25 at index 2

# 3. remove() - removes the first occurrence of a specified element 
my_list.remove(30)


# 4. pop() - removes and returns the element at a specified position (default is last element)
last_element = my_list.pop()  # removes last element

# 5. index() - returns the index of the first occurrence of a specified element and returns -1 if not found
index_of_40 = my_list.index(40)
# 6. sort() - sorts the list in ascending order

# 7. reverse() - reverses the order of the list

# 8. count() - returns the number of occurrences of a specified element
count_of_20 = my_list.count(20)
#


my_list_copy = my_list  # created a reference copy of my_list

# i need new independent copy of my_list so that changes made to new list do not reflect in old list
new_list = my_list.copy()  # creates a shallow copy of my_list

