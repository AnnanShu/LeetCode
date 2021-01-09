#-*- encoding utf-8 -*-
# Author:Anan
class Solution:
    def exist(self, board: list, word: str) -> bool:

        def helper(r_idx, c_idx, board, word, index, visited):
            if index == len(word) : return True
            elif r_idx < 0 or c_idx < 0 or r_idx >= len(board) \
                or c_idx >= len(board[0]):
                return False
            elif visited[r_idx][c_idx]: return False
            elif board[r_idx][c_idx] != word[index]: return False

            visited[r_idx][c_idx] = True
            if helper(r_idx + 1, c_idx, board, word, index + 1, visited) or \
                helper(r_idx, c_idx + 1, board, word, index + 1, visited) or \
                    helper(r_idx - 1, c_idx, board, word, index + 1, visited) or \
                        helper(r_idx, c_idx - 1, board, word, index + 1, visited):
                return True 

            visited[r_idx][c_idx] = False
            return False


        visited = [[False for _ in board[0]] for __ in board]
        for r_idx, row in enumerate(board):
            for c_idx, char in enumerate(row):
                if char == word[0]:
                    index = 0
                    if helper(r_idx, c_idx, board, word, index, visited):
                        return True

        else:
            return False

        
        




