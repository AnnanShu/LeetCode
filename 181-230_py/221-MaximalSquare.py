class Solution:
    def maximalSquare(self, matrix: list) -> int:
        m = len(matrix) + 1
        n = len(matrix[0]) + 1
        dp = [[0 for _ in range(n)] for __ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 +  min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

        maxL = max(dp)
        return maxL * maxL


dp = [[1,2,3,4],[2,3,4,5],[1,2,3,4]]

[i for min_dp in dp for i in min_dp]