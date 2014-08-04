class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        grid = [ [0 for j in range(m)] for i in range(n) ]
        
        for i in range(n):
            for j in range(m):
                if i==0:
                    grid[i][j]=1
                else:
                    if j==0:
                        grid[i][j] = grid[i-1][j]
                    else:
                        grid[i][j] = grid[i-1][j]+grid[i][j-1]
                        
        return grid[-1][-1]