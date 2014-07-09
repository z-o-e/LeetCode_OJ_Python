# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):

        return self.dfs(root, 0)
        
    def dfs(self, root, cursum):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return cursum*10 + root.val
        
        return self.dfs(root.left, cursum*10 + root.val) + self.dfs(root.right, cursum*10 + root.val)    
        