class Solution:
    # @param s, a string
    # @param D, a set of string
    # @return a boolean
    def wordBreak(self, s, D):
        
        return self.dfs(0,0,s,D) 
    
    def dfs(self, preIdx, curIdx, s, D):
        if curIdx==len(s)-1:
            if s[preIdx:curIdx+1] in D:
                return True
            else:
                return False
                
        if s[preIdx:curIdx+1] in D:
            return self.dfs(curIdx+1, curIdx+1, s, D)
  
        else:
            return self.dfs(preIdx, curIdx+1, s, D)
            

