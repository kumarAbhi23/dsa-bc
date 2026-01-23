'''
var arguments = arguments passed to a function when it is called
we can pass variable number of arguments to a function using *args and **kwargs
*args : non keyword variable length arguments :underlying data structure is tuple
**kwargs : keyword variable length arguments  : underlying data structure is dictionary



'''

def sum_all(*args):
    total=0
    for num in args:
        total += num
    return total
result = sum_all(1,2,3,4,5)
print("Sum of all numbers is:", result)

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="New York")        