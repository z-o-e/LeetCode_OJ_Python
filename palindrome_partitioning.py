class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        res, cur = [], []
        start, end = 0, len(s)

        self.dfs(s, start, end, cur, res)
        
        return res
        
    def dfs(self,s,  start, end, cur, res):
        if start==end:
            tmp = cur[:]
            res.append(tmp)
            return
        
        for i in range(start, end):
            if self.isPalindrome(s, start, i):
                cur.append(s[start:i+1])
                self.dfs(s, i+1, end, cur, res)
                cur.pop()
                
    def isPalindrome(self, s, start, end):
        while start<end:
            if s[start]!=s[end]:
                return False
            start+= 1
            end -=1
            
        return True
        
        
        