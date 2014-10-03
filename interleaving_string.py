class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s3)!=len(s1)+len(s2):
            return False
        if not s1 and not s2 and not s3:
            return True
            
        l1,l2 = len(s1), len(s2)
        # D[i][j] = (s3[i+j]==s1[i] and D[i-1][j]) or (s3[i+j]==s2[j] and D[i][j-1]) using 1 indexing for simplicity
        D = [[False for i in range(l2+1)] for j in range(l1+1)]
        D[0][0] = True
        for i in range(l1+1):
            for j in range(l2+1):
                if i==0 and j>0:
                    D[i][j] = s3[i+j-1]==s2[j-1] and D[i][j-1]
                elif j==0 and i>0:
                    D[i][j] = s3[i+j-1]==s1[i-1] and D[i-1][j]
                elif i>0 and j>0:
                    D[i][j] = (s3[i+j-1]==s2[j-1] and D[i][j-1]) or (s3[i+j-1]==s1[i-1] and D[i-1][j])
                
        return D[-1][-1]
