'''
Docstring for DSA_.Array.02_rainWaterTrapping

[3,0,2,0,4]

to trap water we need  left wall,right wall  and water level will be limited by shorter wall

we need find min(leftMax,rightMax)-current_h

 '''
'''
 lets see approch 
          for ith element we need to findMaxLeft and righMax and take min of those 
          and subtract current we will get unit 

          conside these as wall left wall and right wall and in between wall water will be trap 
          water level limited by shorter wall

          for every ith wall we need to find leftMax and rightMax 

          min(rightMax,leftMax)-ith wall height
          

'''      




def rainWaterB(arr):
    # for every element we need to find leftMax and RightMax
    total=0
    for i in range(len(arr)):
        left_max=max(arr[:i+1])
        right_max=max(arr[i:])
        total+=min(left_max,right_max)-arr[i]
    
    return total

arr=[0,1,0,2,1,0,1,3,2,1,2,1]
# print(rainWaterB(arr))

# this program is taking order N^2 As time complexity 

# can we have better approch in finding left max and right max 

'''
we can use two pointer 
l=0 and r=n-1
we will shrink space 
lets see two cases 
cas1: if arr[l]<arr[r]: means left side is limiting wall and right is taller 
       so water will depend on left max
       left_max=max(left_max,arr[i])
       total_water+=left_max-arr[i]
case2: if arr[i]>=arr[j]:
       i.e right side is smaller so water depend on right_max
              


'''
def rainWaterO(arr):
    l,r=0,len(arr)-1
    rightMax=leftMax=0
    total_water=0
    
    
    while(l<r):
        # case 1: if arr[l]<arr[r]
        if arr[l]<arr[r]:
            leftMax=max(leftMax,arr[l])
            total_water+=leftMax-arr[l]
            l+=1
        else:
            rightMax=max(rightMax,arr[r])
            total_water+=rightMax-arr[r]
            r-=1    
    return total_water

    
print(rainWaterO(arr))        