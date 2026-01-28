'''

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal
and all the elements on the secondary diagonal 
that are not part of the primary diagonal.

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

diagonal element if mat[i][j] where i==j and 
     n=3
(0,0).      (0,2)       ->mat[i][n-i-1].    --> j=n-1-i or j+i=n-1
(1,1).      (1,1).        mat[i][3-1-1] mat[1][1]
(2,2)....   (2,0).        mat[i][3-2-1] mat[2][0]

[00 01 02]
[10 11 12]
[20 21 22]

4*4 matrix 
(0,0).      (0,3)
(1,1).      (1,2)
(2,2).      (2,1)
(3,4).      (3,0)

[00 01 02 03]
[10 11 12 13]
[20 21 22 24]
[30 31 33 34]

# we need to handle odd size matrix also where one element can be repated while travesersing 
# diagonal

if n % 2 == 1:
    s -= mat[n//2][n//2]




'''

# bruteforce approch taking O(n^2) time 
def matrixDiogSumB(mat):
     n=len(mat)
     sum=0
     for i in range(n):
           for j in range(n):
                if i==j:
                     sum+=mat[i][j]
                if j+i==n-1:
                     sum+=mat[i][n-i-1]
     if n % 2 == 1:
         sum -= mat[n//2][n//2]                
     return sum                
                


# if we can some how write j in term of j 

# i+j=n-1  ... we no need travese full just need j=n-1-i
'''
  sum+=mat[i][i]. if i==j
  and  j=n-1-i if i!=j
  sum+=mat[i][j]
  
'''

def matrixDiogonalSumO(mat):
     
     sum=0
     n=len(mat) # as square matrix 
     for i in range(n):
          sum+=mat[i][i]  # condition 1
          # calculate j 
          j=n-1-i        # condition 1
          if i!=j:         # to avoid duplicate
               sum+=mat[i][j]
    
     return sum     
     

mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]

# print(matrixDiogSumB(mat))

print(matrixDiogonalSumO(mat))