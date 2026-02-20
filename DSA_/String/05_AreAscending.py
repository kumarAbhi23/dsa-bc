'''
A sentence is a list of tokens separated by a single space with no leading or trailing spaces.
Every token is either a positive number consisting of digits 0-9 with no leading zeros, or a word consisting of lowercase English letters.

For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens: "2" and "4" are numbers 
and the other tokens such as "puppy" are words.
Given a string s representing a sentence,
you need to check if all the numbers in s are strictly increasing from left to right (i.e., other than the last number, each number is strictly smaller than the number on its right in s).


'''

def areNumbersAscending(s):
    # we first split the string into tokens using split() method
    tokens=s.split() # it will take O(n) time complexity and O(n) 
    #space complexity because we are creating a list of tokens from the string
    # it will return list of string 
    # take a least number 
    prev = float('-inf')
    for token in tokens:
        if token.isdigit(): # method used to check a string contains a number (0-9) strig.isdidgit()
            num = int (token)
            if num<=prev:
                return False 
            prev=num
            
    return True        

s="5 box has 3 blue 4 red 6 green and 12 yellow marbles"    
print(areNumbersAscending(s))
