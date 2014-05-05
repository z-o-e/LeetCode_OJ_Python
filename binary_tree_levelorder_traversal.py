# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        res = []
        if root==None:
            return res
        
        # use 2 queues to store nodes of current and next level: currentL, nextL 
        currentL = [root]
        
        while currentL:
            nextL = []
            tmp = []
            for i in range(len(currentL)):
                node = currentL[0]
                tmp.append(node.val)
                currentL = currentL[1:]
                if node.left:
                    nextL += [node.left] 
                if node.right:
                    nextL += [node.right] 
            res.append(tmp)
            currentL = nextL
        
        return res
            