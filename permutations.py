class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        numL = len(num)
        
        if numL==0:
            return
        if numL==1:
            return [num]
            
        res = []
        for i in range(numL):
            for j in self.permute( num[:i]+num[i+1:] ):
                res.append( [num[i]] + j)
                
        return res