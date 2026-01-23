'''
Docstring for 03loops_prblm.06

calculate factorial of a given number using while loop


'''

number=int(input("Enter a number: "))
factorial=1

while number>0:
    factorial*=number
    number-=1

print("Factorial is:",factorial)    
