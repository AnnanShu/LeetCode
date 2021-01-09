from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(the_list):
            for c in the_list:
                the_set = set()
                if c != '.':
                    if c not in the_set:
                        the_set.add(c)
                    else:
                        return False
            
            return True
        
        # check row
        for i in range(9):
            if not check(board[i]):
                return False
        
        # check colom
        for i in range(9):
            candi = [board[j][i] for j in range(9)]
            if not check(candi):
                return False

        
        # check block
        for i_start in range(0, 9, 3):
            for j_start in range(0, 9, 3):
                candi = [board[i][j] for i in range(i_start, i_start+3) for \
                            j in range(j_start, j_start + 3)]

                if not check(candi):
                    return False
        
        return True

a = set()
a.add("8")
a

def check(the_list):
    the_set = set()
    for c in the_list:
        if c != '.':
            print(f"{c}, {the_set}")
            print(c not in the_set)
            if c not in the_set:
                the_set.add(c)
            else:
                return False
    return True

        
board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# check colom
[board[j][0] for j in range(9)]
check([board[j][0] for j in range(9)])
for i in range(9):
    candi = [board[j][i] for j in range(9)]
    print(check(candi))
