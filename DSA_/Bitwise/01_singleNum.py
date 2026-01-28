'''

Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.
You must implement 
a solution with a linear runtime complexity and use only constant extra space.

Input 1: nums = [2,2,1]
Output 1: 1
Explanation 1: 1 is present only once.
'''

'''
properties of bitwise xor 

A	B	A XOR B
0	0	  0
0	1	  1
1	0	  1
1	1	  0


'''

def singleNumB(arr):
    # we will se first burute force approch 
    # we need to return duplicate elemet 
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
        if count==1:
            return arr[i]
    # this approch is taking O(N^2)
#print(singleNumB([2,2,1]))        


# we can optimize it furter we can use hashmap and store count of numer of element 

def singleNumBetter(arr):
       freq={}
       for i in arr:
           freq[i]= freq.get(i,0)+1  # we set default to 0 +1
           #{2: 2, 1: 1}
           # i=2 then in in freq[2]= as key  is not present...so default value =0 and  0+1=1 so,freq[2]=1
           #i=2 as  as key is presnet so in freq[key] =value (value 1)+1= 2...so,freq[2]=2
           
           # what this line is doing freq[i] -key we assing some value 
           #Give me the value of this key.dict.get(key, default)
            #If the key does not exist, return the default value instead of error.
       for key,value in freq.items():
           if value==1:
               return key 
    # this apprcoh is taking O(N) time and O(N) SPACE        
           

def singleNumO(arr):
    res=0
    for i in arr:
        res^=i
    return res
     # this will take O(N) TIME AND O(1) SPACE   
print(singleNumO([2,2,4]))  