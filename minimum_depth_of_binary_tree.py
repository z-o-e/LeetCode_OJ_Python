# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root==None:
            return 0
            
        left, right = 0,0
        
        if root.left!=None:
            left = self.minDepth(root.left)
        if root.right!=None:
            right = self.minDepth(root.right)
            
        if root.left!=None and root.right!=None:
            return min(left, right)+1
        elif root.left==None:
            return right+1
        else:
            return left+1
            
        return 1
        