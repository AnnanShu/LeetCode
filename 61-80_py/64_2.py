from typing import List
from numpy import np
import itertools

class Solution:
    def minPathSum(self, grid: List[List[int]]):
        row = len(grid)
        col = len(grid[0])
        dp = grid.copy()
        for idx, elem in enumerate(dp[0][1:], start=1):
            dp[0][idx] = dp[0][idx-1] + elem

        for idx, elem in enumerate(dp[1:], start=1):
            dp[idx][0] = dp[idx-1][0] + elem[0]

        print(dp)

        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j-1])

        
        return dp

class Solution2:
    def minPathSum(self, grid:List[List[int]]):
        rows = len(grid)
        cols = len(grid[0])
        if not grid:
            return 0
        dp = [[0] * cols for _ in range(rows)]
        dp[0] = list(itertools.accumulate(grid[0]))
        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            for j in range(1, cols):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[-1][-1]







grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
list(itertools.accumulate(grid[0]))
Solution2().minPathSum(grid)