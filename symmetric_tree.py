# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root==None:
            return True
        left = root.left
        right = root.right
        
        return self.checkSymmetric(left, right)
            
    def checkSymmetric(self, left, right):
        if left==None and right==None:
            return True
        elif left==None or right==None:
            return False
        
        return left.val==right.val and self.checkSymmetric(left.left, right.right) and self.checkSymmetric(left.right, right.left)
        