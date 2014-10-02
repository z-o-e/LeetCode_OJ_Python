class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        nrow, ncol = len(matrix), len(matrix[0])
        # h the height array, ncol+1 space
        h, res = [0]*(ncol+1), 0
        
        for i in range(nrow):
            # stack stores the column idx of the height array
            stack = []
            for j in range(ncol+1):
                if j<ncol:
                    if matrix[i][j]=='1':
                        h[j]+= 1
                    else:
                        h[j]=0
                      
                if not stack or h[j] >= h[stack[-1]]:
                    stack.append(j)
                else:
                    while stack and h[j]<h[stack[-1]]:
                        prevIdx = stack.pop()
                        if not stack:
                            area = h[prevIdx]*j
                        else:
                            area = h[prevIdx]*(j-1-stack[-1])
                            
                        res = max(res, area)
                    stack.append(j)
             
        return res
