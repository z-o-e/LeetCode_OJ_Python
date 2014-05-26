class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        # check rows and cols
        bag = {}
        for i in range(81):
            bag[i] = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in bag[i] or board[i][j] in bag[j+9]:
                        return False
                    else:
                        if board[i][j] not in bag[i]:
                            bag[i].append(board[i][j]) 
                        if board[i][j] not in bag[j+9]:
                            bag[j+9].append(board[i][j]) 
        
        # check squares                    
        for a in range(0,9,3):
            for b in range(0,9,3):
                bag = []
                for i in range(3):
                    for j in range(3):
                        if board[a+i][b+j] != '.':
                            if board[a+i][b+j] in bag:
                                return False
                            else:
                                bag.append(board[a+i][b+j])
                                
        return True