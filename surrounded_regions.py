class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board==[] or len(board[0])<2:
            return 
        
        numCol, numRow = len(board[0]), len(board)
        allO = [[False for j in range(numCol)] for i in range(numRow)]
        
        # only O-paths extending from borders would remain  
        queue = []
        for j in range(numCol):
            # top border
            if board[0][j] == 'O':
                allO[0][j] = True
                queue.append([0,j])
            
            # bottom border    
            if board[-1][j] == 'O':
                allO[-1][j] = True
                queue.append([numRow-1,j])                
        
        for i in range(numRow):
            # left border
            if board[i][0] == 'O':
                allO[i][0] = True
                queue.append([i,0])
            
            # right border
            if board[i][-1] == 'O':
                allO[i][-1] = True
                queue.append([i, numCol-1])
        
        # BFS        
        while queue:
            [i,j] = queue.pop()
            
            # search up
            if i-1>0 and board[i-1][j]=='O' and not allO[i-1][j]:
                allO[i-1][j] = True
                queue.append([i-1,j])
            # search down
            if i+1<numRow and board[i+1][j]=='O' and not allO[i+1][j]:
                allO[i+1][j] = True
                queue.append([i+1,j])
            # search left
            if j-1>0 and board[i][j-1]=='O' and not allO[i][j-1]:
                allO[i][j-1] = True
                queue.append([i,j-1])
            # search right
            if j+1<numCol and board[i][j+1]=='O' and not allO[i][j+1]:
                allO[i][j+1] = True
                queue.append([i,j+1])

        for i in range(numRow):
            for j in range(numCol):
                if allO[i][j]==False and board[i][j]=='O':
                    board[i][j] = 'X'
                    
        return 