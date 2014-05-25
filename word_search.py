class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        height, width  = len(board), len(board[0])
        
        for i in range(height):
            for j in range(width):
                if board[i][j]== word[0]:
                    if self.dfs( i, j ,board, word[1:]):
                        return True
                    
        return False
                    
    def dfs(self, i , j, board, word):
        if not len(word):
            return True
         
        # search up 
        if i<len(board)-1 and board[i+1][j]==word[0]:
            # avoid duplicate, mark board[i][j] visited with "!"
            tmp, board[i][j] = board[i][j], "!"
            if self.dfs(i+1, j, board, word[1:]):
                return True
            # recover if not match
            board[i][j] = tmp
        
        # search down
        if i>0 and board[i-1][j]==word[0]:
            tmp, board[i][j] = board[i][j], "!"
            if self.dfs(i-1, j, board, word[1:]):
                return True
            board[i][j] = tmp
        
        # search left
        if j>0 and board[i][j-1]==word[0]:
            tmp, board[i][j] = board[i][j], "!"
            if self.dfs(i, j-1, board, word[1:]):
                return True
            board[i][j] = tmp
            
        # search right
        if j<len(board[0])-1 and board[i][j+1]==word[0]:
            tmp, board[i][j] = board[i][j], "!"
            if self.dfs(i, j+1, board, word[1:]):
                return True
            board[i][j] = tmp
            
        return False
        