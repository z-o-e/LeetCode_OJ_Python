class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        res = [ [0 for i in range(n)] for i in range(n)]
        
        cur, x,y , last = 1, 0,0, n*n

        while cur <= last:
            for i in range(n):
                res[x][y+i] = cur
                cur += 1
                
            if cur >= last: break
        
            for i in range(n-1):        
                res[x+1+i][y+n-1] = cur
                cur += 1
                
            for i in range(n-1):        
                res[x+n-1][y+n-2-i] = cur
                cur += 1
        
            for i in range(n-2):
                res[x+n-2-i][y] = cur
                cur += 1
                
            x += 1
            y += 1
            n -= 2
                
        return res
                            