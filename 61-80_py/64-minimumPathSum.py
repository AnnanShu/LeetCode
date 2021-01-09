class Solution:
    def minPathSum(self, grid: list):
        row = len(grid)
        col = len(grid[0])
        # dp = [grid[0] + [[grid[i][0]] + [0] * (col-1) for i in range(1, row)]]
        dp = grid.copy()
        for idx, elem in enumerate(dp[0][1:], start=1):
            dp[0][idx] = dp[0][idx-1] + elem

        for idx, elem in enumerate(dp[1:], start=1):
            dp[idx][0] = dp[idx-1][0] + elem[0]

        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j-1])

        return dp


grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
m = 3
n = 3

dp = [grid[0]] + [[grid[i][0]] + [0]*(n-1) for i in range(1,m)]
dp


Solution().minPathSum(list1)
