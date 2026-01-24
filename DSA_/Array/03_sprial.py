'''
Given an n*n matrix print element in sprial pattern


'''
'''
for any m*n matrix

mat=[ 0,1,2,4
    0[1,2,3,4],
    1[4,5,6,11],
    3[7,8,9,34],
    
]




'''


def printSpiral(mat):
      # define 4 ptr 
      top=left=0
      btm=len(mat)-1
      right=len(mat[0])-1
      
      lst=[]
      while(left<=right and top<=btm):
           # left to right
           for i in range(left,right+1):
                 lst.append(mat[top][i])
                # print(f"at it range value of i is {i}", mat[top][i])
           top+=1 
           # top to bootm  
            
           for i in range(top,btm+1):
                lst.append(mat[i][right])
           right-=1 
           # right to left 
           # but first check is there is any row left 
           if top<=btm:  
             for i in range(right,left-1,-1):
                   lst.append(mat[btm][i])
             btm-=1
           #btm to top
           # check if col exits or not 
           if left<=right:
               for i in range(btm,top-1,-1):
                  lst.append(mat[i][left])
               left+=1        
      return lst    
         


mat=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
    
]



print(printSpiral(mat))

