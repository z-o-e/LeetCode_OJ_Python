# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        res = []
        if root==None:
            return res
        
        cursum, curseq = 0, []
        
        self.dfs(root, sum, cursum, curseq, res)
        
        return res
        
        
    def dfs(self, root, sum, cursum, curseq, res):
        cursum  += root.val
        curseq.append(root.val)
        
        if root.left==None and root.right==None and cursum==sum:
            tmp = curseq[:]
            res.append(tmp)
            curseq = curseq[:-1]
            return 
        
        if root.left!=None:
            self.dfs(root.left, sum, cursum, curseq, res)
        
        if root.right!=None:
            self.dfs(root.right, sum, cursum, curseq, res)
            
        curseq = curseq[:-1]
                