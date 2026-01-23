'''
Docstring for 03loops_prblm.05

find the first non repeated charecter in a given string

 
'''

input_str = "swwiiss"
first_non_repeated_char = None

for char in input_str:
    if input_str.count(char)==1:
        first_non_repeated_char = char
        break   

print("First non-repeated character:", first_non_repeated_char)