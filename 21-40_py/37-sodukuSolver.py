"""
inout: [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]

"""
from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]):
        """
        Do not return anything, modify board in-place instead.
        """
        curr_exist = 0
        for line in board:
            for num in line:
                if num.isdigit(): curr_exist += 1
        candi = set([str(i + 1) for i in range(9)])
        def line_pos(i):
            return set(board[i])
        def col_pos(j):
            return set([board[i][j] for i in range(9)])
        def square_pos(i, j):
            i_start = (i // 3) * 3
            j_start = (j // 3) * 3
            the_square = [board[i][j] for i in range(i_start, i_start+3) for \
                            j in range(j_start, j_start + 3)]
            return set(the_square)

        while curr_exist < 81:
            flag = False
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        remaining = candi - line_pos(i) - col_pos(j) -  square_pos(i, j)
                        if len(remaining) == 1:
                            board[i][j] = list(remaining)[0]
                            curr_exist += 1
                            flag = True
            i
        return board

Solution().solveSudoku(board)
            
set([str(i + 1) for i in range(9)]) - set(['1','2'])
['1','2']

board = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

board2 = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]

Solution().solveSudoku(board2)
def square_pos(i, j):
    i_start = (i // 3) * 3
    j_start = (j // 3) * 3
    print(f"i_start : {i_start}, j_start : {j_start}")
    the_square = list()
    # for j in range(j_start, j_start + 3):
    #     for i in range(i_start, i_start + 3):
    #         print(f"i:{i}, j:{j}")
    #         the_square.append(board[i][j])
    the_square = [board[i][j] for i in range(i_start, i_start+3) for \
                    j in range(j_start, j_start + 3)]
    return the_square

square_pos(7, 7)

11 % 10

