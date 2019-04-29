# Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

# The binary search tree is guaranteed to have unique values.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root!=None:
            if root.val>=L and root.val<=R:
                return root.val+self.rangeSumBST(root.left,L,R)+self.rangeSumBST(root.right,L,R)
            elif root.val>R:
                return self.rangeSumBST(root.left,L,R)
            else:
                return self.rangeSumBST(root.right,L,R)
        else:
            return 0