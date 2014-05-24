class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        
        res = [1] + [0] * rowIndex
    
        for i in range(1,rowIndex + 1):
            res[i] = 1
            # DP from backwords!
            for j in range(i-1, 0, -1 ):
                res[j] += res[j-1]
            
        return res
        