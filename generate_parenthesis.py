class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        self.res, self.n = [], n
        
        self.dfs('', 0, 0)
        
        return self.res
        
    def dfs(self, s, left, right):
        if self.n==left==right:
            self.res.append(s)
            return 
        if left<self.n:
            self.dfs(s+'(', left+1, right)
        if right<left and right<self.n:
            self.dfs(s+')', left, right+1)
            
        return 