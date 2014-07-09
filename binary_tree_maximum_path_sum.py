# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        res = [root.val]
        
        self.dfs(root,res)
        
        return res[0]
            
    def dfs(self, root, res):
        if root==None:
            return 
            
        l = self.dfs(root.left,res)
        r = self.dfs(root.right,res)
        new_val = root.val
        if l>0:
            new_val += l
        if r>0:
            new_val += r
        
        res[0] = max(res[0], new_val)
        
        if max(l,r)>0:
            return max(l,r)+root.val
        
        return root.val