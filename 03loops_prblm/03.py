'''
Docstring for 03loops_prblm.03

multiplication table of given number upto 10 and skip 5th multiple


'''

number=int(input("Enter a number: "))

for i in range(1,11):
    if i==5:
        continue
    print(number,"x",i,"=",number*i)

