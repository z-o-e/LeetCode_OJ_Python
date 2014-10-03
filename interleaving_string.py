class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s3)!=len(s1)+len(s2):
            return False
        
        p1, p2, i = 0, 0, 0
        
        while p1<len(s1) and p2<len(s2):
            if s3[i]!=s1[p1] and s3[i]!=s2[p2]:
                return False
            elif s3[i]==s1[p1] and s3[i]!=s2[p2]:
                p1 +=1
                i += 1
            elif s3[i]==s2[p2] and s3[i]!=s1[p1]:
                p2 +=1
                i += 1
            else:
                return self.isInterleave(s1[p1+1:], s2[p2:], s3[i+1:]) or self.isInterleave(s1[p1:], s2[p2+1:], s3[i+1:])
                
        return True


