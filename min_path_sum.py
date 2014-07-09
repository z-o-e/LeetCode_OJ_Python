class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid): 
        m,n = len(grid), len(grid[0])
        f = [ [0 for i in range(n)] for i in range(m) ] 
        
        f[0][0] = grid[0][0]
        for i in range(1,n,1):
            f[0][i] = grid[0][i]+f[0][i-1]    
        for i in range(1,m,1):
            f[i][0] = f[i-1][0]+grid[i][0]
            
        for i in range(1,m,1):
            for j in range(1,n,1):
                f[i][j] = grid[i][j]+min(f[i-1][j], f[i][j-1])
                
        return f[-1][-1]
