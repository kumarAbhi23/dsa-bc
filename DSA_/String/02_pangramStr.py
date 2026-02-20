'''
A string is called a pangram if it contains every letter of the English alphabet at least once. For example, "The quick brown fox jumps over the lazy dog" is a pangram because it contains all the letters from 'a' to 'z'.

'''

def isPanagra(s):
    #convert string to lower case
    s=s.lower()
    # create a set of all characters in the string
    char_set=set(s)
    #print(len(char_set)) # 27 because it also include space and dot
    
    # check if the set contains all the letters from 'a' to 'z'
    for char in range(ord('a'),ord('z')+1):
        if chr(char) not in char_set:
            return False
    return True



print(isPanagra("The quick brown fox jumps over the lazy dog"))
