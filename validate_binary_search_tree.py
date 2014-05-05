class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.check(-10**10,root,10**10)
        
    def check(self,smallNum,root,bigNum):
        if root==None:
            return True
        if not smallNum<root.val<bigNum:
            return False
        return self.check(root.val,root.right,bigNum) and self.check(smallNum,root.left,root.val)