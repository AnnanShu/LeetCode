class Solution:
    def solveNQueens(self, n : int):
        board = [['.']* n for _ in range(n)]
        res = []

        def isValid(board, row, col):
            for i in range(col):
                if board[row][i] == 'Q':
                    return False

            i, j = row-1, col -1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                
                i -= 1
                j -= 1
            
            i, j = row - 1, col + 1
            n = len(board[0])
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

        def backtrack(board, row):
            if len(board) == row:
                res.append(board)
            
            n = len(board[row])
            for col in range(n):
                if not isValid(board, row, col):
                    continue
                # select current point as Q
                board[row][col] = 'Q'
                # backtrack operation
                backtrack(board, row + 1)
                board[row][col] = '.'

                    

        backtrack(board, 0)
        return res

    
