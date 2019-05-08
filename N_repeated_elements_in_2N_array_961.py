# In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

# Return the element repeated N times.

 

# Example 1:

# Input: [1,2,3,3]
# Output: 3
# Example 2:

# Input: [2,1,2,5,3,2]
# Output: 2
# Example 3:

# Input: [5,1,5,2,5,3,5,4]
# Output: 5

# Moore's voting algorithm
def repeatedNTimes(A):
    dic = {}
    n = len(A)
    if n==2:
        return None
    for i in A:
        if i in dic.keys():
            dic[i]+=1
        else:
            dic[i]=1
        if dic[i]==(n//2):
            return i
    return None
