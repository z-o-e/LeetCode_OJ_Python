class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        rLen, cLen = len(matrix), len(matrix[0])
        row, col = [False]*rLen, [False]*cLen
        
        for i in range(rLen):
            for j in range(cLen):
                if matrix[i][j]==0:
                    row[i] = True
                    col[j] = True
        
        for i in range(rLen):
            if row[i]:
                matrix[i] = [0]*cLen
                
        for j in range(cLen):
            if col[j]:
                for i in range(rLen):
                    matrix[i][j]=0