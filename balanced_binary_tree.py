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
        
        if self.dfs(root)==-1:
            return False
            
        return True
    
    def dfs(self, root):
        if root==None:
            return 0
            
        left = self.dfs(root.left)
        if left==-1:
            return -1
        
        right = self.dfs(root.right)
        if right==-1:
            return -1
            
        if abs(left-right)>1:
            return -1
        return max(left, right) + 1
        