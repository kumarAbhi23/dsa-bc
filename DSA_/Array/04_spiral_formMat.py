'''

Given a positive integer n, generate an n x n matrix filled with elements
from 1 to n2 in spiral order.


Input 1: n = 3
Output 1: [[1,2,3],[8,9,4],[7,6,5]]

we will follow same approch of spiral travesing insted appending to list we will use 
a counter 

define 2-d martrix

mat=[[0]*n for i in range(n)]


'''

def spiralForm(n):
    # first create an empty 
    mat=[[0]*n for _ in range(n)]
    # print(mat)
    
    # now we will define 4 var for spiral pattern 
    left=top=0
    btm=right=n-1
    counter=1

    while(left<=right and top<=btm):
        # left to right 
        for i in range(left,right+1):
            mat[top][i]=counter
            counter+=1
        top+=1    
        # top to bottom
        for i in range(top,btm+1):
            mat[i][right]=counter
            counter+=1
        right-=1
        
        # right to left but check is any row is there 
        if left<=right:
            for i in range(right,left-1,-1):
                mat[btm][i]=counter
                counter+=1
            btm-=1
        # btm to top again we will check if there is col or not
        if top<=btm:
            for i in range(btm,top-1,-1):
                mat[i][left]=counter
                counter+=1
            left+=1
    return mat        

mat=spiralForm(3) 
print(mat)
   
       



