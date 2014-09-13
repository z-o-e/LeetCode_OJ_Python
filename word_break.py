class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        
        return self.dfs(0,0,s,dict) 
    
    def dfs(self, preIdx, curIdx, s, dict):
        if curIdx==len(s)-1:
            print 'c1'
            if s[preIdx:curIdx+1] in dict:
                return True
            else:
                return False
                
        if s[preIdx:curIdx+1] in dict:
            return self.dfs(curIdx+1, curIdx+1, s, dict)
  
        else:
            return self.dfs(preIdx, curIdx+1, s, dict)
            

                        