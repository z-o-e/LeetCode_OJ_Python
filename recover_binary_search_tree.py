# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        orig, stack = root, []
        prev = first = second = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if prev and root.val<prev.val:
                    if first==None:
                        first, second = prev, root
                    else:
                        second = root
                prev, root = root, root.right
        first.val, second.val = second.val, first.val
        return orig
                
        