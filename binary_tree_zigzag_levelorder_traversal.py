# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        res = []
        if root==None:
            return res
        
        # similar to level order, except for adding var for direction
        right = 1
        currentL = [root]
        
        while currentL:
            nextL = []
            tmp = []
            
            for i in range(len(currentL)):
                # left to right
                if right==1:
                    node = currentL[0]
                    currentL = currentL[1:]
                    if node.left:   nextL += [node.left]
                    if node.right:  nextL += [node.right]
                
                # right to left
                else:
                    node = currentL[-1]
                    currentL = currentL[:-1]
                    if node.right:  nextL = [node.right]+ nextL
                    if node.left:   nextL = [node.left]+ nextL
                
                tmp.append(node.val)    
            
            # flip direction
            right*=-1
            
            res.append(tmp)
            currentL = nextL
        
        return res
                