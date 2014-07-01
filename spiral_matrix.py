class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        res = []
        if len(matrix)==0:
            return res
        
        x,y = 0,0
        row,col, total = len(matrix), len(matrix[0]), len(matrix)*len(matrix[0])
        
        while len(res) < total:
            for i in range(col):
                res.append(matrix[x][y+i])
            
            if len(res) >= total:   break
            
            for i in range(row-1):
                res.append(matrix[x+1+i][y+col-1])
                
            if len(res) >= total:   break
                
            for i in range(col-1):
                res.append(matrix[x+row-1][y+col-2-i])
            
            if len(res) >= total:   break
                
            for i in range(row-2):
                res.append(matrix[x+row-2-i][y])
            
            x += 1
            y += 1
            col -= 2
            row -= 2
            
        return res
            