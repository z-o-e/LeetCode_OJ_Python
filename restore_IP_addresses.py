class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        res = []
        
        if len(s)<4 or len(s)>12:
            return res
        
        if int(s[:3])<256 and s[0]!="0":
            cur = [s[:3]]
            res = self.restore(s[3:], cur, res)
        
        if s[0]!="0":
            cur = [s[:2]]
            res = self.restore(s[2:],cur, res)
        
        cur = [s[0]]
        res = self.restore(s[1:],cur, res)
        
        return res
        

    def restore(self, s, cur, res):
        if s=="":
            if len(cur)==4:
                cur = ".".join(cur)
                if cur not in res:
                    res.append(cur)
            
        else:
            if len(cur)<4:
                
                if len(s)>2 and int(s[:3])<256 and s[0]!="0":
                    tmp = cur[:]
                    tmp.append(s[:3])
                    res = self.restore(s[3:], tmp, res)

                
                if len(s)>1 and s[0]!="0":
                    tmp = cur[:]
                    tmp.append(s[:2])
                    res = self.restore(s[2:], tmp, res)
            
                cur.append(s[0])
                res = self.restore(s[1:],cur,res)

    
        return res
