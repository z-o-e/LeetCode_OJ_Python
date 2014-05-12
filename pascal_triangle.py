class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        res = []
        
        for i in range(numRows):
            line = []
            
            for j in range(i+1):
                if j == 0 or j == i:
                    line.append(1)
                else:
                    line.append(res[i-1][j-1] + res[i-1][j])
            
            res.append(line)
            
        return res
                