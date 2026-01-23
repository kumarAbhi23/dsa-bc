'''
Docstring for 05Functions.02peb


polymorphism in functions: same method but handling two different data types


write a function which can take two number of arguments and also accept multiple strings 
'''

def multiply(a,b):
    return a * b

# multiplying two numbers
num1 = 5
num2 = 10
result_numbers = multiply(num1, num2)
print("Multiplication of numbers:", result_numbers)
# multiplying one strings and one number
str1 = "Hello "

result_strings = multiply(str1,num1)
print("Multiplication of strings:", result_strings)

