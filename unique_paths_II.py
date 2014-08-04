class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0
            
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [ [0 for j in range(n)] for i in range(m) ]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    f[i][j]=0
                else:
                    if i==0:
                        if j==0:
                            f[i][j] = 1
                        else:
                            f[i][j]=f[i][j-1]
                    elif j==0:
                        f[i][j]=f[i-1][j]
                    else:
                        f[i][j] = f[i-1][j]+f[i][j-1]
                        
        return f[-1][-1]
        