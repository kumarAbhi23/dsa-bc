
# case 1:
'''
l1=[1,2,3]
l2=l1
print(l2 is l1)  # True because both point to same object

l2[2]=33

print(l1)  # l1 is also changed because both point to same object

'''


# case 2:

'''
l1=[1,2,3]
l2=l1

print(l2 is l1)  # True because both point to same object

l2=[1,2,3]

print(l2 is l1)  # False because l2 now points to a new object

'''


# case 3:
'''
l1=[1,2,3]
l2=[1,2,3]

print(l2 is l1)  # False because both point to different objects

a=10
b=10
print(a is b)  # True because both point to same object
# As integers are immutable so both a and b point to same object in memory 
# value is cached by python internally
# both a and b point to same memory location


'''

# case 4:
    # copy and deepcopy are used to create a new object in memory
    # so that changes made to new object do not reflect in old object 
    # slice operator creates a shallow copy of list
    
l1=[1,2,3,[4,5]]

l2=l1.copy()  # shallow copy



