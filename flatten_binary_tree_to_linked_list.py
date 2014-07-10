# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root==None:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        if root.left==None:
            return 
        
        leftT = root.left
        rightT = root.right
        while leftT.right!=None:
            # find the right most node of the left subtree
            leftT = leftT.right
        # append rightsubtree to the rightmost node of leftsubtree    
        leftT.right = root.right
        root.right = root.left
        root.left = None
        