
'''
what is valid anagram?

two strings are anagrams if they contain the same characters but in different order.
For example, "listen" and "silent" are anagrams because they contain the
same characters (l, i, s, t, e, n) but in a different order.

Note : after sorting both the strings should be same if they are anagrams
but sorting will take O(nlogn) time complexity and O(n) space complexity

'''

# lets do using hashmap

def isVaildAnagram(s,t):
    #both string length should be same 
    if len(s)!=len(t):
        return False
    count ={}
    
    for ch in s:
        count[ch]=count.get(ch,0)+1
    
    # print(count)     
    for ch in t:
        if ch not in count:
            return False
        # it is present 
        count[ch]-=1
        # delete value if its count is 0
        if count[ch]==0:
           del count[ch]
    
    # return true if count is empty else false 
    return len(count)==0    
         
s='anagrama'
t='nagaramb'
print(isVaildAnagram(s,t))         