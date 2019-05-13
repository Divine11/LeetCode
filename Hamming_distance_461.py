# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example:

# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are different.
        
def hammingDistance(x,y):
    mask=1
    su = 0
    is_set_x = False
    is_set_y = False
    for i in range(32):
        if x&(mask<<i)!=0:
            is_set_x = True
        if y&(mask<<i)!=0:
            is_set_y = True
        su += is_set_x^is_set_y
        is_set_x = False
        is_set_y = False
    return su

#Time complexity: O(1)
#Space complextiy: O(1)

hammingDistance(1,4)


