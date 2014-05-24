class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        if s==p:
            return True
        
        endS, endP = len(s), len(p)
        # ss record the last match till '*'
        pointS = pointP  = 0
        # star marks position of '*' in p and ss marks the position s could possibly match up
        star, ss = -1, 0
        
        while pointS<endS:
            if pointP<endP and p[pointP] in ('?',s[pointS]):
                pointP += 1
                pointS += 1
            elif pointP<endP and p[pointP]=='*':
                star = pointP
                pointP += 1
                ss = pointS
            elif star!= -1:
                pointP = star+1
                ss += 1
                pointS = ss
            else:
                return False
        
        # check if the rest of p
        pp = p[pointP:].replace('*','')
        
        return pp==""