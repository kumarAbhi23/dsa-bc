'''
Docstring for DSA_.String.04_palindromeSt

Write a function that checks if a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. The function should return `True` if the string is a palindrome and `False` otherwise.

Input 1: “abcba”
Output 1: true
Explanation 1: The above string remains the same on reading from both ends.
'''

'''
brute forcr approch will be to reverse string and campare with original string 

'''

def isPalindromeB(s):
    # reverse string 
    rev_str=s[::-1] # this will take O(n) time complexity and O(n) space complexity because it creates a new string
    return rev_str==s
# time complexity: O(n) where n is the length of the string
# space complexity: O(n) because we are creating a new string to store the reversed string

def isPalindromeTwoPointer(s):
    left ,right =0,len(s)-1
    while left <right:
        if s[left]!=s[right]:
            return False
        # if equal then incremt/decremnt ptr 
        left+=1
        right-=1
    return True
# time complexity will be O(N)- AND SPACE O(1)
    
s="abcba"
print(isPalindromeTwoPointer(s))
# print(isPalindromeB(s))

