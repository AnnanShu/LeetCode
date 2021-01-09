from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0 
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if memo[i][j] != 0: return memo[i][j]
            candi = []
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = i + dx, j + dy 
                if 0 <= x < m and 0 <= y < n and matrix[i][j] > matrix[x][y]:
                    candi.append([x, y])

            memo[i][j] = max(dfs(a, b) for a, b in candi) + 1 if candi else 1
            return memo[i][j]
        
        for i in range(m):
            for j in range(n):
                dfs(i, j)
        
        return max(max(line) for line in memo)
            