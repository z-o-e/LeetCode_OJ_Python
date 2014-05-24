# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
            
        root = TreeNode(postorder[-1])
        split = inorder.index(postorder[-1])
        
        root.left = self.buildTree(inorder[ :split ], postorder[ :split ])
        root.right = self.buildTree(inorder[split+1:], postorder[ split:-1 ])
        
        return root
        