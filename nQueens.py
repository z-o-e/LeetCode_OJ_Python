class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        if n==1:
            return [['Q']]
        if n<4:
            return []
            
        self.res = []
        board = [ '.'*n for i in range(n) ]
        
        for i in range(n):
            tmp = board[:]
            tmp[0] = '.'*i+'Q'+'.'*(n-i-1)
            self.dp( tmp, 1, n, 0, i)
                    
        return self.res
        
    def dp(self, board, Qnum, n, row, col):
        #print board
        if Qnum==n:
            self.res.append(board)
            return
        
        if row>n-1 or col>n-1:
            return 
            
        tmp = board[:]   
            
        if 'Q' in board[row]:
            if row<n-1:
                self.dp( board, Qnum, n, row+1, 0)
        
        elif 'Q' in ''.join(board[i][col] for i in range(row)):
            if col<n-1:
                self.dp(board, Qnum, n, row, col+1)
            elif col==n-1 and row<n-1:
                self.dp( board, Qnum, n, row+1, 0)
                
        elif 'Q' in ''.join(board[row-i][col-i] for i in range(1,min(row, col)+1)) or 'Q' in ''.join(board[row-i][col+i] for i in range(1,min(row+1, n-col))) :
            if col<n-1:
                self.dp( board, Qnum, n, row, col+1)
            elif col==n-1 and row<n-1:
                self.dp( board, Qnum, n, row+1, 0)   
        
        else:
            if col<=n-1:
                board[row] = board[row][:col]+'Q'+board[row][col+1:]                                
            else:
                if row<n:
                    board[row] = board[row][:col-1]+'Q'
                
            self.dp(board, Qnum+1, n, row+1, 0)  
            self.dp(tmp, Qnum, n, row, col+1) 