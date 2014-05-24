# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        split = inorder.index(preorder[0])
        
        root.left = self.buildTree( preorder[ 1:split+1 ], inorder[ :split ] )
        root.right = self.buildTree( preorder[ split+1: ], inorder[ split+1: ] )
        
        return root