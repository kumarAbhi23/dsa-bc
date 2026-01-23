'''
Docstring for 03loops_prblm.08

prime number : whole number greater than 1 and excatly divisble by itself 

'''

number =int(input('enter number : '))


is_prime=True

if number>1:
  for num in range(2,number):
    if (number%num)==0:
        is_prime=False
        break

print(is_prime)