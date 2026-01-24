'''
Docstring for DSA_.Array.05_concentraionArray

given an array of n length 
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

 

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

ans[i]==nums[i]
and and[i+n]=nums[i]

it is just repeat array two time 
return arr*2. --python way 
-O(n)

or return nums+nums
or below sol 

'''

def concentraionArray(arr):
    
        # create an empty lst of size 2*n
        # not don't use insert as it will first go to ith index then insert and shifiting of 
        # element also will be there it will leads to increase time to n^2
        ans_arry_size=2*(len(arr))
        ansArray=[]
        i=j=0
        while j<=ans_arry_size-1:
            # first pre-check
            if i<=len(arr)-1:
                ansArray.append(arr[i])
                i+=1
                j+=1
            if i>len(arr)-1:
                i=0    
        return ansArray

arr=[1,2,1]
print(concentraionArray(arr))  
          
        

