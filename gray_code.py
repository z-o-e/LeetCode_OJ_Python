class Solution:
    # @return a list of integers
    def grayCode(self, n):
        res = []
        for i in range(pow(2,n)):
            res.append(self.convertD2G(i))
            
        return res
    
    def convertD2G(self,n):
        return (n>>1)^n
        