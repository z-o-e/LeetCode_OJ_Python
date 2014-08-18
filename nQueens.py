class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.res = []
        
        self.solver(0, [-1]*n, n)
        
        return self.res
    
    def solver(self, idx, board, n):
        # current state board[i]=j indicates 'Q' placed at position i-th row, j-th column
        if idx==n:
            r = ['.'*n for i in range(n)]
            for i in range(n):
                if board[i]==n-1:
                    r[i] = r[i][:n-1]+'Q'
                else:
                    r[i] = r[i][:board[i]]+'Q'+r[i][board[i]+1:]
            self.res.append(r)
            return 
        
        # for each position before n,
        #   place queen
        #   if current state is valid, then place next queen solver(depth+1, n)     
        for i in range(n):
            board[idx] = i
            if (self.isValid(idx, board)):
                # increment line
                self.solver(idx+1, board, n)
                
    def isValid(self, idx, board):
        for i in range(idx):
            # same column or same diagnol
            if board[i]==board[idx] or abs(board[i]-board[idx])==abs(idx-i):
                return False
        return True
            