# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if not root:
            return 0
        
        left, right = 0, 0
        
        if root.left:
            left = self.maxDepth(root.left)
        
        if root.right:
            right = self.maxDepth(root.right)
            
        return max(right,left) + 1
        