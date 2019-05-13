# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

# Example 1:

# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Example 2:

# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 

# Note:

# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.

def sortedSquares(A):
    j = 0
    while j<len(A) and A[j]<0:
        j+=1
    j = j-1
    i = j+1
    ans  = [None]*(len(A))
    k=0
    while i<len(A) and j>=0:
        if A[i]**2>A[j]**2:
            ans[k] = A[j]**2
            k+=1
            j-=1
        else:
            ans[k] = A[i]**2
            k+=1
            i+=1
    while i<len(A):
       ans[k]=A[i]**2
       k+=1
       i+=1
    while j>=0:
        ans[k]=A[j]**2
        k+=1
        j-=1
    return ans

## Time complexity: O(n)
## Space complexity: O(n)

print(sortedSquares([-4,-2,-1,0,1,2]))