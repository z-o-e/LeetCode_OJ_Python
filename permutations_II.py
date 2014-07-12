class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        numL = len(num)
        if numL==0:
            return 
        if numL==1:
            return [num]
        
        num.sort()    
        res = []
        prev = None
        
        for i in range(numL):
            if num[i]==prev:
                continue
            prev = num[i]
            for j in self.permuteUnique(num[:i]+num[i+1:]):
                res.append( [num[i]] + j )
                    
        return res