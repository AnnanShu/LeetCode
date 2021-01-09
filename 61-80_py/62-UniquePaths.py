# Dynamic Programming
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]

        return dp[m-1][n-1]

print(Solution().uniquePaths(7,3))














# Recursive Solution
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        row, col = 1, 1
        count = []

        def auxiliary_func(row, col, m, n):
            if row < m and col < n:
                auxiliary_func(row+1, col, m, n)
                auxiliary_func(row, col+1, m, n)

            elif row < m:
                auxiliary_func(row+1, col, m, n)

            elif col < n:
                auxiliary_func(row, col+1, m, n)

            else:
                count.append(1)

        if m == 1 and n == 1: return 1
        if row < m:
            auxiliary_func(row + 1, col, m, n)
        if col < n:
            auxiliary_func(row, col + 1, m, n)

        return len(count)



