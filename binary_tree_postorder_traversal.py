# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        res = []
        if root==None:
            return res
        stack, pre = [root], None
        
        while stack:
            cur = stack[-1]
            # nodes with no subtrees or have been visited
            if (cur.left==None and cur.right==None) or (pre!=None and pre in (cur.left, cur.right)):
                res.append(stack.pop().val)
                pre = cur
            else:
                if cur.right!=None:
                    stack.append(cur.right)
                if cur.left!=None:
                    stack.append(cur.left)
                    
        return res
                