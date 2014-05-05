class Solution:
    # @return an integer
    def numTrees(self, n):
        f = [0]*(n+1)
        f[0] = 1
        f[1] = 1
        for i in range(2,n+1):
            for k in range(1,i+1):
                f[i] += f[k-1]*f[i-k]
    
        return f[n]