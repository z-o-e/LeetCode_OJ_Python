class Solution:
    # @return a string
    def countAndSay(self, n):     
        cur = "1"
        if n==1:
            return cur
            
        for i in range(n-1):
            nxt = self.transform(cur)
            cur = nxt
        
        return cur
        
    def transform(self,s):
        idx, res = 0, ""
        while idx<len(s):
            l, num = 1, s[idx]
            while idx+1<len(s) and num==s[idx+1]:
                idx += 1
                l += 1
            idx += 1
            res += str(l)+str(num)
        
        return res