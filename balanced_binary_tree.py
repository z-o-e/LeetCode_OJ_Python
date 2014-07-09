# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root==None:
            return True
        
        diff = abs(self.dfs(root.left)-self.dfs(root.right))
        
        if diff>1:
            return False
            
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def dfs(self, root):
        if root==None:
            return 0
            
        return max(self.dfs(root.left), self.dfs(root.right) ) + 1
        