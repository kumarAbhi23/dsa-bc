'''

Reverse bits of a given 32 bits signed integer.

Input: n = 43261596

Output: 964176192

Explanation:

Integer	Binary
43261596	00000010100101000001111010011100

964176192	00111001011110000010100101000000

# take a bit and add to res =0 

we  will take a bit from number  n&1= git ab bit -lsb 
shift existing bit 1 postion so can append a bit  (res<<1)

res = (res<<1)|(n&1)



'''

def reveseBit(n):
    # we are taking 
    #n = n & 0xFFFFFFFF
    res=0
    for i in range(32):
        res = (res<<1)| (n&1)
        # also we need to drop used bit 
        n=n>>1 # used to drop 1  bit from lsb 
    return res    

n=43261596
print(reveseBit(n))


