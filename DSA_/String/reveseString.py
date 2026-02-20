# https://leetcode.com/problems/reverse-words-in-a-string/description/

'''
Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words.
Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
'''
'''
s=" the sky is blue  "
s=s.strip() # this will take O(n) time complexity and O(1) space complexity
s=s.split() # this will take O(n) time complexity and O(n) space complexity

#revese the list
s=s[::-1] # this will take O(n) time complexity and O(n) space complexity
# if we want to reverse the list in place then we can use two pointers approach

print(s)
# convert list to string 
s=" ".join(s) # this will take O(n) time complexity and O(n) space complexity
print(s)
    
# time complexity: O(n)
# space complexity: O(n)
# if we want to reverse the list in place then 
# we can use two pointers approach and the space complexity will be O(1)
    
'''

def reveseWord(str):
      # spilt string using split()- remove all space leading and traling also multiple 
      # space also handled so no worry  and give list 
      
      words=str.split()
      # revese list : slicing will give new list 
      # so do inplace 
      i,j =0,len(words)-1
      while i<j:
          words[i],words[j]=words[j],words[i]
          i+=1
          j-=1
      return " ".join(words)    
  
print(reveseWord("hello   woeld  "))  
  
  