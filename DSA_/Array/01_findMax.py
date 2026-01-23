'''
Given an array of N positive number  task is find maxium value of 
|arr[i] -arr[j]| +|i-j|

we are taking absolute value so |i-j| is same as |j-i|


ex: n=4 [4,5,6,8]

o/: 4

'''
'''
brute forece approch take one element and iterate in loop 

# if i=4 then possible value of j will {4,5,6,8}
# but if both i and j have same value then result will 0
# ex: [4,5,6,8] i=1 and j=1then |arr[i] -arr[j]| +|i-j|
#                                   4-4 +1-1=0

# if i =1 then j should i+1 and 

# if i =3 i.e pointing to last then no j possible so we don't take that 


# outer loop i=0 to range(n-1) and inner loop j=i+1 to range(n)


'''
def findMaxBrute(arr):
    max_ele=0
    n=len(arr)
    for i in range(0,n-1):
       
        for j in range(i+1,n):
            max_so_far=abs(arr[i]-arr[j])+abs(i-j)
            max_ele=max(max_ele,max_so_far)
            
        
    return max_ele

# time complexity of above program is is O(n^2)



'''
let's see another approch 
|arr[i] - arr[j]| - can be +(arr[i] - arr[j]) , -(arr[i] - arr[j])



similarly |i-j| - can be (i-j), -(i-j)

arr[i] - arr[j] + i -j  -->    arr[i]+i -( arr[j]+j )

arr[i] - arr[j] -i+j    -->   arr[i]-i -(arr[j]-j)

arr[j]-arr[i] +i-j     -->    arr[j]-j -(arr[i]-i)

arr[j]-arr[i] -i+j     -->    arr[j]+j -(arr[i]+i)


i,j are just varaible we can replace i and j as they are just number


# generalise: arr[i]+i or arr[i]-i

we need to find 
max1=max(arr[i]+i) ,min1=min(arr[i]+i)
max(arr[i]-i) ,min(arr[i]-i)
 
we need to find max(max1-min1,max2-min2)
'''

def findMaxO(arr):
    n=len(arr)
    max1=float('-inf') # negative infinty 
    min1=float('inf') # positive infinity 
    max2=float('-inf')
    min2=float('inf')
    
    for i in range(0,n):
        temp1=arr[i]+i
        temp2=arr[i]-i
        max1=max(temp1,max1)
        min1=min(temp1,min1)
        
        max2=max(temp2,max2)
        min2=min(temp2,min2)
    
    return max(max1-min1,max2-min2)    



arr=[4,5,6,8]
print(findMaxO(arr))


    
    






         



