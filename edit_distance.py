class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        
        l1, l2 = len(word1)+1, len(word2)+1
        f = [[0 for j in range(l2)] for i in range(l1)]
        
        for i in range(l1):
            for j in range(l2):
                if i==0:
                    f[i][j] = j
                elif j==0:
                    f[i][j] = i
                else:
                    if word1[i-1]==word2[j-1]:
                        f[i][j] = f[i-1][j-1]
                    else:
                        f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1])+1
        return f[-1][-1]
        