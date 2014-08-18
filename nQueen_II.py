class Solution:
    # @return an integer
    def totalNQueens(self, n):
        self.res = 0
        board = [-1]*n
        
        self.solver(0, board, n)

        return self.res        
        
    def solver(self, cur, board, n):
        if cur==n:
            self.res += 1
            return
        
        for i in range(n):
            board[cur]=i
            if self.isValid(cur,board):
                self.solver(cur+1, board, n)
        
            
    def isValid(self, cur, board):
        for i in range(cur):
            if board[i]==board[cur] or abs(i-cur)==abs(board[i]-board[cur]):
                return False
        return True